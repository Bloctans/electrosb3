local Util = {}

function Util.FromScratch(Position)
    return Vector2.new(Position.X + 240, -Position.Y + 180)
end

function Util.Compare(A,B)
    local NA = tonumber(A)
    local NB = tonumber(B)
    
    if not (NA and NB) then
        local SA = tostring(A)
        local SB = tostring(B)

        if SA < SB then
            return -1
        elseif SA > SB then
            return 1
        else
            return 0
        end
    end 

    return NA - NB
end

return Util