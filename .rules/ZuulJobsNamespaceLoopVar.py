from ansiblelint import AnsibleLintRule


class ZuulJobsNamespaceLoopVar(AnsibleLintRule):

    id = 'ZUULJOBS0001'
    shortdesc = 'Loop vars should have zj_ prefix'
    description = """
Check for tasks that does not follow
the policy of namespacing loop variables with zj_ prefix.
See: \
https://zuul-ci.org/docs/zuul-jobs/policy.html\
#ansible-loops-in-roles
"""

    tags = {'zuul-jobs-namespace-loop-var'}

    def matchplay(self, file, task):
        results = []
        if file.get('type') not in ('tasks', 'handlers'):
            return results

        has_loop = 'loop' in task
        for key in task.keys():
            if key.startswith('with_'):
                has_loop = True

        if has_loop:
            if 'loop_control' not in task:
                results.append(("", self.shortdesc))
            elif 'loop_var' not in task.get('loop_control'):
                results.append(("", self.shortdesc))
            elif not task.get('loop_control')\
                    .get('loop_var').startswith('zj_'):
                results.append(("", self.shortdesc))
        return results
