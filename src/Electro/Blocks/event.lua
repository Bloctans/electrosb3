local Enum = Electro.Enum
local Event = {}

function Event.Broadcast(Args, API)
    API:StartHats("event_whenbroadcastreceived", {
        BROADCAST_OPTION = Args.BROADCAST_INPUT
    })
end

function Event.BroadcastAndWait(Args, API)
    local Info = API:GetScriptInfo()

    if (not Info.StartBroadcast) then
        Info.StartBroadcast = true

        Info.Scripts = API:StartHats("event_whenbroadcastreceived", {
            BROADCAST_OPTION = Args.BROADCAST_INPUT
        })
    end

    local ShouldYield = false

    for _, v in pairs(Info.Scripts) do
        if v.State ~= Enum.STATUS_DONE then
            ShouldYield = true
        end
    end

    if ShouldYield then
        API:Yield()
    else
        Info.StartBroadcast = false
        Info.Scripts = {}
    end
end

function Event.OnMouseClick()
    local Stepper = Electro.BlockEngine.Stepper

    for _, Sprite in pairs(Electro.Renderer.RenderTargets) do
        if Electro.Util.CheckAABB(Sprite.Rect, Electro.MouseRect) then
            Stepper.EachHat("event_whenthisspriteclicked", function(Hat)
                if Hat.Sprite == Sprite:GetRootSprite() then
                    Stepper.CreateScript(Hat, Sprite)
                end
            end)
        end
    end
end

Event.Events = {
    MouseClick = Event.OnMouseClick
}

Event.Definitions = {
    ["whenflagclicked"] = {
        Type = Enum.BLOCK_HAT
    },
    ["broadcast"] = {
        Type = Enum.BLOCK_STACK,
        Function = Event.Broadcast
    },
    ["broadcastandwait"] = {
        Type = Enum.BLOCK_STACK,
        Function = Event.BroadcastAndWait
    },
    ["whenbroadcastreceived"] = {
        Type = Enum.BLOCK_HAT,
        RestartScripts = true,
    },
    ["whenkeypressed"] = {
        Type = Enum.BLOCK_HAT,
    },
    ["whengreaterthan"] = { -- This is stupid, KNOWN, not implemented..
        Type = Enum.BLOCK_HAT
    },
    ["whenthisspriteclicked"] = {
        Type = Enum.BLOCK_HAT,
    }
}

return Event