/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { AppSidebar } from "./sidebar";
import { patch } from "@web/core/utils/patch";

// Add AppSidebar to WebClient's static components
WebClient.components = {
    ...WebClient.components,
    AppSidebar,
};
