from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)

        # Get the command output from the task result
        command_output = task_vars['disk_space_output']['stdout_lines']

        # Append a custom message to the command output
        custom_message = 'This is a custom message.'
        modified_output = command_output + [custom_message]

        # Update the task result with the modified output
        result['changed'] = True
        result['disk_space_output'] = modified_output

        return result
