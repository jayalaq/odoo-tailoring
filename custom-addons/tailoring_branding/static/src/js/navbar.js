/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(NavBar.prototype, {
    toggleHomeMenu() {
        this.env.bus.trigger("TOGGLE_HOME_MENU");
    },
});
