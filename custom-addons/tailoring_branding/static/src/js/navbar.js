/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(NavBar.prototype, {
    toggleHomeMenu() {
        // Find the parent WebClient and toggle its home menu
        // We use the env.bus to communicate
        const webClient = this.__owl__.parent?.component;
        if (webClient && webClient.toggleHomeMenu) {
            webClient.toggleHomeMenu();
        }
    },
});
