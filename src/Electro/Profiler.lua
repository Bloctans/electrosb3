local Profiler = {}

local DeltonInstance

function Profiler.Init()
    DeltonInstance = Delton:new(32)
end

function Profiler.Benchmark(Name)
    local Benchmark = {}

    local Start = love.timer.getTime()

    function Benchmark.End()
        local Diff = love.timer.getTime() - Start

        print("Completed Benchmark: "..Name.." in "..tostring(Diff).." Seconds")
    end

    return Benchmark
end

function Profiler.Start(Name)
    DeltonInstance:start(Name)
end

function Profiler.EndStart(Name)
    DeltonInstance:stop()
    DeltonInstance:start(Name)
end

function Profiler.End()
    DeltonInstance:stop()
end

function Profiler.Present()
    DeltonInstance:present()
end

function Profiler.Render()
    DeltonInstance:step()
end

return Profiler