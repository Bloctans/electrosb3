return function()
    local Sound = {
        Source = nil,
        Name = nil,
        PlayingYield = false, -- Specific to playuntildone
        ID = nil
    }

    function Sound.GetPlaying()
        return Sound.Source:isPlaying()
    end

    function Sound.Stop()
        Sound.Source:stop()
    end

    function Sound.Play()
        assert(Sound.Source, "Attempted to play unloaded sound")
        Sound.Source:stop()
        Sound.Source:play()
    end

    return Sound
end