/** @odoo-module **/

import { Component, useState, useRef, useEffect } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class AppSidebar extends Component {
    static template = "tailoring_branding.AppSidebar";
    static props = {};

    setup() {
        this.menuService = useService("menu");
        this.actionService = useService("action");
        this.state = useState({
            collapsed: false,
            hovering: false,
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
        return !this.state.collapsed || this.state.hovering;
    }

    toggleCollapse() {
        this.state.collapsed = !this.state.collapsed;
    }

    onMouseEnter() {
        if (this.state.collapsed) {
            this.state.hovering = true;
        }
    }

    onMouseLeave() {
        this.state.hovering = false;
    }

    selectApp(app) {
        this.menuService.selectMenu(app);
    }

    getMenuItemHref(payload) {
        return `/odoo/${payload.actionPath || "action-" + payload.actionID}`;
    }
}
