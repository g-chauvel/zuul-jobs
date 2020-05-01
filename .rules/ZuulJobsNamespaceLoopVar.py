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

    def matchtask(self, file, task):
        if file.get('type') != 'tasks':
            return False

        has_loop = 'loop' in task
        for key in task.keys():
            if key.startswith('with_'):
                has_loop = True

        if has_loop:
            if 'loop_control' not in task:
                return True
            elif 'loop_var' not in task.get('loop_control'):
                return True
            elif not task.get('loop_control')\
                    .get('loop_var').startswith('zj_'):
                return True
        return False
