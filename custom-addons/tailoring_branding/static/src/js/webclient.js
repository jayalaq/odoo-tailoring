/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { AppSidebar } from "./sidebar";
import { patch } from "@web/core/utils/patch";

// Patch the WebClient class to add AppSidebar component
patch(WebClient, {
    components: {
        ...WebClient.components,
        AppSidebar,
    },
});
