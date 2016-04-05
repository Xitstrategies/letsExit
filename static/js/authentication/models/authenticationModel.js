import can from 'can';
import map from 'can.map';
import Model from 'can.model';

export default Model.extend({
    route: 'v1/accounts',

},{
    define:{
        username: {},
        password: {},
        confirm_password: {},
        email: {},
        first_name: {
            serialize: false
        },
        last_name: {
            serialize: false
        },
        client_name: {
            serialize: false
        },
        client_id: {
            serialize: false
        },
        created_at: {
            serialize: false
        },
        updated_at: {
            serialize: false
        }
    }

})
