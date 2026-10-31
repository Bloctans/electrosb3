local Util = {}

function Util.FromScratch(Position)
    return Vector2.new(Position.X + 240, -Position.Y + 180)
end

function Util.ToScratch(Position)
    return Vector2.new(Position.X - 240, -Position.Y + 180)
end

function Util.TableMod(Value, Table)
    return ((Value-1) % table.length(Table)) + 1
end

function Util.ToBoolean(Value)
    if type(Value) == "boolean" then
        return Value
    elseif type(Value) == "string" then
        if Value == "" or Value == "0" or string.lower(Value) == "false" then
            return false
        end
    elseif type(Value) == "number" then
        return Value > 0
    end

    return Value and true or false
end

function Util.CheckAABB(Rect1, Rect2)
    local Result = (Rect1.X1 > Rect2.X1) and (Rect1.X2 < Rect2.X2)
        and (Rect1.Y1 > Rect2.Y1) and (Rect1.Y2 < Rect2.Y2)

    if Rect1.Invert or Rect2.Invert then
        return not Result
    else
        return Result
    end
end

function Util.Rect(Position, Size, Opposing)
    return {
        X1 = Position.X,
        Y1 = Position.Y,
        X2 = Position.X + Size.X,
        Y2 = Position.Y + Size.Y,
        Invert = Opposing
    }
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