#!/usr/bin/env python3


class Part:
    def __init__(self, ratings):
        self.ratings = ratings
        self.accepted = False
        self.rejected = False
        self.next_workflow = "in"

    def __repr__(self):
        return repr(("Part ratings: ", (self.ratings)))

    def accept(self):
        self.accepted = True

    def reject(self):
        self.rejected = True

    def set_next_workflow(self, id):
        self.next_workflow = id

    def score(self):
        score = 0
        for r in ["a", "s", "m", "x"]:
            score += self.ratings.get(r, 0)
        return score


class Workflow:
    def __init__(self, id, filters, if_fail):
        self.id = id
        self.filters = filters
        self.if_fail = if_fail

    def __repr__(self):
        return repr(("Workflow: ", self.id, self.filters, self.if_fail))

    def test_part(self, part):
        p = part
        for f in self.filters:
            if f.test == "<":
                if p.ratings.get(f.variable) < f.value:
                    return f.if_pass
            elif f.test == "=":
                if p.ratings.get(f.variable) == f.value:
                    return f.if_pass
            elif f.test == ">":
                if p.ratings.get(f.variable) > f.value:
                    return f.if_pass
        return self.if_fail


class Filter:
    def __init__(self, variable, test, value, if_pass):
        self.variable = variable
        self.test = test
        self.value = value
        self.if_pass = if_pass

    def __repr__(self):
        return repr(("Filter: ", self.variable, self.test, self.value, self.if_pass))


class System:
    def __init__(self, data):
        self.accepted_parts = []
        workflows_str, parts = data.split("\n\n")

        workflows_str = workflows_str.split("\n")
        workflows = {}
        for i, wf in enumerate(workflows_str):
            id = wf[: wf.index("{")]

            filters = wf.split("{")[1].split(",")[:-1]
            for ii, f in enumerate(filters):
                var = f[0]
                t = f[1]
                val, if_pass = f[2:].split(":")
                filters[ii] = Filter(
                    variable=var, test=t, value=int(val), if_pass=if_pass
                )

            f = wf[:-1].split(",")[-1]
            workflows[id] = Workflow(id=id, filters=filters, if_fail=f)
        self.workflows = workflows

        parts = parts.split("\n")
        for i, part in enumerate(parts):
            ratings = {}
            ratings_str = part.strip("{").strip("}").split(",")
            for ii, r in enumerate(ratings_str):
                ratings[r[0]] = int(r[2:])
            parts[i] = Part(ratings=ratings)
        self.parts = parts

    def __repr__(self):
        return repr(("System: Workflows: ", self.workflows, "Parts: ", self.parts))

    def run(self):
        for p in self.parts:
            print("Run part ", p)
            go = not (p.accepted or p.rejected)
            while go:
                result = self.run_next_workflow(part=p)
                print("Result ", result)
                if result == "A":
                    self.accepted_parts.append(p)
                    p.accept()
                    go = False
                elif result == "R":
                    p.reject()
                    go = False
                else:
                    p.set_next_workflow(id=result)

    def run_next_workflow(self, part):
        wf_id = part.next_workflow
        result = self.workflows.get(wf_id).test_part(part=part)
        return result

    def score(self):
        score = 0
        for p in self.accepted_parts:
            score += p.score()
        return score
