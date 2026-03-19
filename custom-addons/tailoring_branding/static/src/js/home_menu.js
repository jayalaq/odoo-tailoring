/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class HomeMenu extends Component {
    static template = "tailoring_branding.HomeMenu";
    static props = {
        onAppSelected: { type: Function, optional: true },
    };

    setup() {
        this.menuService = useService("menu");
    }

    get apps() {
        return this.menuService.getApps();
    }

    selectApp(app) {
        this.menuService.selectMenu(app);
        if (this.props.onAppSelected) {
            this.props.onAppSelected();
        }
    }

    getMenuItemHref(payload) {
        return `/odoo/${payload.actionPath || "action-" + payload.actionID}`;
    }
}
