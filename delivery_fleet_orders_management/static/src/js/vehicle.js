odoo.define('fleet_vechile.print_ins', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var rpc = require('web.rpc');
    var Dialog = require('web.Dialog');

    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.oe_send_notifications').click(this.proxy('action_def'));
            }
        },
        action_def: function () {
            var self = this;
            return rpc.query({
                model: 'fleet.vehicle',
                method: 'odoo_button_click_send_notifications'
            }).then(function (res) {
                console.log(res);
                Dialog.alert(self, "Notification Sent To Our Driver notify THem with the pending Orders!", {
                        title: 'Pending Orders Notifications',
                    });
            });

        }
    });
});