#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            num1=dict(type='int', required=True),
            num2=dict(type='int', required=True)
        )
    )
    
    num1 = module.params['num1']
    num2 = module.params['num2']

    result = num1 + num2
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()