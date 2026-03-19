/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { HomeMenu } from "./home_menu";
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

// Register HomeMenu as a known component
WebClient.components = {
    ...WebClient.components,
    HomeMenu,
};

// Patch the WebClient prototype to add home menu state and logic
patch(WebClient.prototype, {
    setup() {
        super.setup();
        this.homeMenuState = useState({ open: false });

        // Toggle home menu from navbar button
        this.env.bus.addEventListener("TOGGLE_HOME_MENU", () => {
            this.homeMenuState.open = !this.homeMenuState.open;
        });

        // Close home menu when an app is selected
        this.env.bus.addEventListener("MENUS:APP-CHANGED", () => {
            this.homeMenuState.open = false;
        });
    },

    onHomeAppSelected() {
        this.homeMenuState.open = false;
    },
});
