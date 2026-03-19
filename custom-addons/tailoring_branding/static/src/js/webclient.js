/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { HomeMenu } from "./home_menu";
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

// Add HomeMenu to WebClient's static components
WebClient.components = {
    ...WebClient.components,
    HomeMenu,
};

// Patch the WebClient prototype to add home menu state
patch(WebClient.prototype, {
    setup() {
        super.setup(...arguments);
        this.homeMenuState = useState({ open: false });

        // Open home menu when no app is loaded
        this.env.bus.addEventListener("WEBCLIENT:SHOW_HOME_MENU", () => {
            this.homeMenuState.open = true;
        });

        // Close home menu when an app is selected
        this.env.bus.addEventListener("MENUS:APP-CHANGED", () => {
            this.homeMenuState.open = false;
        });
    },

    toggleHomeMenu() {
        this.homeMenuState.open = !this.homeMenuState.open;
    },

    onHomeAppSelected() {
        this.homeMenuState.open = false;
    },
});
