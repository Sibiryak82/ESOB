
local function ternaryExpression(b, v1, v2)
    local res = nil
    if b then
        res = v1;
    else
        res = v2;
    end
    
    return res;
end



Indicator = {}
 
-------------------------------------------------------------------------------------------------
--  Initialize Variables --
-------------------------------------------------------------------------------------------------
-- 1: isReady

-- 2: haveDamageShield
-- 3: haveEnoughHealth
-- 4: haveEnoughMagicka
-- 5: haveEnoughStamina

-- 6: currentBar
-- 7: isTargetingEnemy

-- 8: targetInShortRange
-- 9: targetIn LongRange
-- 10: can use ultimate
-- 11: sp1

-- 12: target is in front
-- 13: target is behind
-- 14: target is at right
-- 15: target is at left
-------------------------------------------------------------------------------------------------


Indicator.name = "Indicator"
Indicator.version = 1
Indicator.targetX = 0.0
Indicator.targetY = 0.0


Indicator.gameIsReady = 1
Indicator.haveDamageShield = 0
Indicator.haveEnoughHealth = 0
Indicator.haveEnoughMagicka = 0
Indicator.haveEnoughStamina = 0
Indicator.currentBar = 0
Indicator.isTargetingEnemy = 0
Indicator.inShortRange = 0
Indicator.inLongRange = 0
Indicator.canUseUlt = 0
Indicator.sp1 = 0



Indicator.target_is_in_front = 0
Indicator.target_is_behind = 0
Indicator.target_is_at_right = 0
Indicator.target_is_at_left = 0


Indicator.target_set = false




function Indicator.setBasicResources()
     local currentSTAMINA, maxSTAMINA = GetUnitPower("player", POWERTYPE_STAMINA)
     local currentHEALTH, maxHEALTH = GetUnitPower("player", POWERTYPE_HEALTH)
     local currentMAGICKA, maxMAGICKA = GetUnitPower("player", POWERTYPE_MAGICKA)
     local shield = GetUnitAttributeVisualizerEffectInfo('player', ATTRIBUTE_VISUAL_POWER_SHIELDING, STAT_MITIGATION, ATTRIBUTE_HEALTH,
     POWERTYPE_HEALTH) or 0
     
     
     Indicator.haveDamageShield = ternaryExpression(shield > 0.15 * maxHEALTH, 1, 0)
     Indicator.haveEnoughHealth = ternaryExpression(currentHEALTH > 0.7 * maxHEALTH, 1, 0)
     Indicator.haveEnoughMagicka = ternaryExpression(currentMAGICKA > 0.4 * maxMAGICKA, 1, 0)
     Indicator.haveEnoughStamina = ternaryExpression(currentSTAMINA > 0.4 * maxSTAMINA, 1, 0)
     Indicator.currentBar = ternaryExpression(GetActiveHotbarCategory() == 0, 1, 0)
     
     
     local currentULT, maxULT, effectiveMaxULT = GetUnitPower("player", POWERTYPE_ULTIMATE)
     Indicator.canUseUlt = ternaryExpression(currentULT >= GetSlotAbilityCost(8), 1, 0)
     
end

     
function Indicator.setIsTargetingEnemy()
     current, max, effectiveMax = GetUnitPower("reticleover", POWERTYPE_HEALTH)
     Indicator.isTargetingEnemy = ternaryExpression((GetUnitName("reticleover") ~= "") and (current > 2) and (GetUnitReaction("reticleover") == UNIT_REACTION_HOSTILE), 1, 0)
 
 end
 
 
 
 function Indicator.setRangeAndSp1()
 
     Indicator.inShortRange = 0
     Indicator.inLongRange = 0
     
      -- sp1: sorcerer, crystal fragments proc
     Indicator.sp1 = 0
     
     
     local minRange = 10000
     local minRangeSlot = 0
     local maxRange = 0
     local maxRangeSlot = 0
     
     if Indicator.isTargetingEnemy == 1 then
        for i=3, 8 do
            local id=GetSlotBoundId(i)
            if id == 114716 then Indicator.sp1 = 1 end
    
            local AminRange,AmaxRange=GetAbilityRange(id)
            if AmaxRange>0 then
                if AmaxRange < minRange then
                    minRangeSlot = i
                    minRange = AmaxRange
                end
                
                if AmaxRange > maxRange then
                    maxRangeSlot = i
                    maxRange = AmaxRange
                end
            end
            
        end
        
          

        
    end
    
    
    if minRangeSlot ~= 0 then
         Indicator.inShortRange = ternaryExpression(HasRangeFailure(minRangeSlot), 0, 1)
    end
    
    if maxRangeSlot ~= 0 then
        Indicator.inLongRange = ternaryExpression(HasRangeFailure(maxRangeSlot), 0, 1)
    end
 
 end
 
 
 function Indicator.getFirstTeammateLoc()
         for i = 1, GROUP_SIZE_MAX do
            local unitTag = ZO_Group_GetUnitTagForGroupIndex(i)
            local x, y, heading = GetMapPlayerPosition(unitTag)
            local isMe = AreUnitsEqual("player", unitTag)

            if (DoesUnitExist(unitTag) and (not isMe) and (GetGroupMemberSelectedRole(unitTag) == 1)) then
                 Indicator.targetX = x
                 Indicator.targetY = y
                 return
            end
        
        end
        
        if (not Indicator.target_set) then
            local x, y = GetMapPlayerPosition("player")
            Indicator.targetX = x
            Indicator.targetY = y
        end
 
 end
 
 
 
 function Indicator.set_related_direction()
 
        local distance = 1.2
 
 
        Indicator.target_is_in_front = 0
        Indicator.target_is_behind = 0
        Indicator.target_is_at_right = 0
        Indicator.target_is_at_left = 0



        local x, y = GetMapPlayerPosition("player")
        local cameraHeading = GetPlayerCameraHeading()
        local h = -(cameraHeading + 0.5 * 3.14159265358)
        
        dx = -(x - Indicator.targetX)
        dy = y - Indicator.targetY

                
        rx = (dx * math.cos(h) - dy * math.sin(h)) * 1000
        ry = (dx * math.sin(h) + dy * math.cos(h)) * 1000

        
        if rx > distance then
            Indicator.target_is_in_front = 1
        elseif rx < -distance then
            Indicator.target_is_behind = 1
        
        end
        
        if ry > distance then
            Indicator.target_is_at_left = 1
        elseif ry < -distance then
            Indicator.target_is_at_right = 1
        end
                
        
    end
 
 
 
 function Indicator.Update()

     Indicator.setBasicResources()
     Indicator.setIsTargetingEnemy()
     Indicator.setRangeAndSp1()
     
     Indicator.getFirstTeammateLoc()
     Indicator.set_related_direction()

     
     IW1:SetValue(Indicator.gameIsReady)
     
     IW2:SetValue(Indicator.haveDamageShield)
     IW3:SetValue(Indicator.haveEnoughHealth)
     IW4:SetValue(Indicator.haveEnoughMagicka)
     IW5:SetValue(Indicator.haveEnoughStamina)
     
     IW6:SetValue(Indicator.currentBar)
     IW7:SetValue(Indicator.isTargetingEnemy)
     
     IW8:SetValue(Indicator.inShortRange)
     IW9:SetValue(Indicator.inLongRange)
     
     IW10:SetValue(Indicator.canUseUlt)
     IW11:SetValue(Indicator.sp1)
     
     IW12:SetValue(Indicator.target_is_in_front)
     IW13:SetValue(Indicator.target_is_behind)
     IW14:SetValue(Indicator.target_is_at_right)
     IW15:SetValue(Indicator.target_is_at_left)
               
               
 end
 
 function upDate()
 
 Indicator.Update()
 

 zo_callLater(function()
    upDate()
 end, 100)
 
 end
 
 
 
-------------------------------------------------------------------------------------------------
--  OnAddOnLoaded  --
-------------------------------------------------------------------------------------------------
function Indicator.OnAddOnLoaded(event, addonName)
   if addonName ~= Indicator.name then return end
 
    Indicator:Initialize()
    
    SLASH_COMMANDS["/myprint"] = function()
        for i = 1, GROUP_SIZE_MAX do
            local unitTag = ZO_Group_GetUnitTagForGroupIndex(i)
            local name = GetUnitName(unitTag)
            local x, y, heading = GetMapPlayerPosition(unitTag)
            local zone = GetUnitZone(unitTag)
            local isMe = AreUnitsEqual("player", unitTag)

            if (DoesUnitExist(unitTag)) then
            d(name.."x: "..x.."y: "..y.."  "..GetGroupMemberSelectedRole(unitTag)) -- dd:1, heal:4, tank:2
            end
        
        end
    end
    

    
    SLASH_COMMANDS["/setl"] = function()
        d("setl")
        Indicator.target_set = true
        local x, y = GetMapPlayerPosition("player")
        Indicator.targetX = x
        Indicator.targetY = y
        
    end
    
    SLASH_COMMANDS["/unsetl"] = function()
        d("unsetl")
        Indicator.target_set = false
    end
    
    
    SLASH_COMMANDS["/mytest"] = function()
        for i = 1, 5 do
            d(i)
            
        end
    end

    
end
 
-------------------------------------------------------------------------------------------------
--  Initialize Function --
-------------------------------------------------------------------------------------------------
function Indicator:Initialize()
 
EVENT_MANAGER:UnregisterForEvent(Indicator.name, EVENT_ADD_ON_LOADED)

upDate()



end
 
-------------------------------------------------------------------------------------------------
--  Register Events --
-------------------------------------------------------------------------------------------------
EVENT_MANAGER:RegisterForEvent(Indicator.name, EVENT_ADD_ON_LOADED, Indicator.OnAddOnLoaded)

