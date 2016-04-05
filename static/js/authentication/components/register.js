import can from 'can';
import Component from 'can.component';
import registerIndex from '../../templates/authentication/register.stache';
import RegisterModel from '../models/authenticationModel';

export default can.Component.extend({
    tag: 'register-user',
    template: can.stache(registerIndex),
    viewModel: {
        username: '',
        password: '',
        email: '',
        registerUser: function(vm) {
            var user = new RegisterModel({
                username: vm.username,
                password: vm.password,
                email: vm.email
            });
            user.save();
        }
    }
});
