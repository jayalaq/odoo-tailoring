/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class AppSidebar extends Component {
    static template = "tailoring_branding.AppSidebar";
    static props = {};

    setup() {
        this.menuService = useService("menu");
        this.actionService = useService("action");
        this.state = useState({
            collapsed: false,
        });

        this.env.bus.addEventListener("MENUS:APP-CHANGED", () => this.render());
    }

    get apps() {
        return this.menuService.getApps();
    }

    get currentApp() {
        return this.menuService.getCurrentApp();
    }

    get isExpanded() {
        return !this.state.collapsed;
    }

    toggleCollapse() {
        this.state.collapsed = !this.state.collapsed;
        document.body.classList.toggle("tc_sidebar_collapsed", this.state.collapsed);
    }

    selectApp(app) {
        this.menuService.selectMenu(app);
    }

    getMenuItemHref(payload) {
        return `/odoo/${payload.actionPath || "action-" + payload.actionID}`;
    }
}
