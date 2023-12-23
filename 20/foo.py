#!/usr/bin/env python3


class Module:
    def __init__(self, id, destinations):
        self.pulsed = {"low": 0, "high": 0}
        self.id = id
        self.destinations = destinations
        self.untyped = True
        self.flipflop = False
        self.conjunction = False
        self.broadcaster = False
        if id == "broadcaster":
            self.untyped = False
            self.broadcaster = True
        self.on = None
        self.last = None

    def __repr__(self):
        if self.untyped:
            return repr((self.id, "Untyped", self.destinations))
        elif self.flipflop:
            return repr((self.id, "Flip-flop %", self.on, self.destinations))
        elif self.conjunction:
            return repr((self.id, "Conjunction &", self.last, self.destinations))
        elif self.broadcaster:
            return repr((self.id, "Broadaster", self.destinations))
        else:
            return repr("err")

    def set_type(self, type):
        if type == "%":
            self.untyped = False
            self.flipflop = True
            self.conjunction = False
            self.on = False
        if type == "&":
            self.untyped = False
            self.flipflop = False
            self.conjunction = True
            self.last = {}

    def init_last(self, key):
        self.last[key] = "low"

    def pulse(self, frm, signal):
        self.pulsed[signal] += 1
        if self.flipflop == True and signal == "low":
            if self.on == True:
                self.on = False
                result = [(self.id, a, "low") for a in self.destinations]
                return result
            elif self.on == False:
                self.on = True
                result = [(self.id, a, "high") for a in self.destinations]
                return result
        elif self.flipflop == True and signal == "high":
            return []
        elif self.conjunction == True:
            self.last[frm] = signal
            print(frm, signal, self)
            if "low" in self.last.values():
                result = [(self.id, a, "high") for a in self.destinations]
                return result
            else:
                result = [(self.id, a, "low") for a in self.destinations]
                return result
        elif self.broadcaster == True:
            result = [(self.id, a, signal) for a in self.destinations]
            return result
        elif self.untyped == True:
            result = []
            return result


class Configuration:
    def __init__(self, data):
        self.module_ids = []
        self.modules = {}
        destinations = []
        lines = data.split("\n")
        for line in lines:
            t = None
            m, dlist = line.split(" -> ")
            if "%" in m or "&" in m:
                t = m[0]
                m = m[1:]
            dlist = [a.strip() for a in dlist.split(",")]
            module = Module(id=m, destinations=dlist)
            if t:
                module.set_type(type=t)
            self.module_ids.append(m)
            self.modules[m] = module
            destinations.extend(dlist)
        destinations = list(set(destinations))
        for d in destinations:
            if not self.modules.get(d):
                module = Module(id=d, destinations=[])
                self.modules[d] = module
        for m in self.modules.values():
            for d in m.destinations:
                dm = self.modules.get(d)
                if dm.conjunction == True:
                    dm.init_last(key=m.id)
        for i in range(0, 1000):
            self.run_from_button()

    def run_from_button(self):
        queue = [("button", "broadcaster", "low")]
        keep_going = True
        while queue:
            # print(queue)
            frm, to, signal = queue.pop(0)
            print("Pulse: ", frm, signal, " -> ", to)
            m = self.modules.get(to)
            result = m.pulse(frm=frm, signal=signal)
            queue.extend(result)
            if len(queue) == 0:
                keep_going = False

    def __repr__(self):
        return repr((self.module_ids, self.modules))

    # todo: write def score() function to multiply pulses
    def score(self):
        low = 0
        high = 0
        for m in self.modules.values():
            low += m.pulsed.get("low")
            high += m.pulsed.get("high")
        return low, high, low * high
