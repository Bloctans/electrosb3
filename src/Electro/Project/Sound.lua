return function()
    local Sound = {
        Source = nil,
        Name = nil
    }

    function Sound.Play()
        assert(Sound.Source, "Attempted to play unloaded sound")
        Sound.Source:play()
    end

    return Sound
end