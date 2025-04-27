/*!
 * Socket.IO v3.0.4
 * (c) 2014-2020 Guillermo Rauch
 * Released under the MIT License.
 */
!(function (t, e) {
    if (typeof exports === "object" && typeof module === "object") {
        module.exports = e();
    } else if (typeof define === "function" && define.amd) {
        define([], e);
    } else if (typeof exports === "object") {
        exports.io = e();
    } else {
        t.io = e();
    }
})(
    typeof self !== "undefined"
        ? self
        : typeof window !== "undefined"
        ? window
        : typeof global !== "undefined"
        ? global
        : Function("return this")(),
    function () {
        return function (t) {
            var e = {};

            function n(r) {
                if (e[r]) return e[r].exports;
                var o = (e[r] = {
                    i: r,
                    l: false,
                    exports: {},
                });
                t[r].call(o.exports, o, o.exports, n);
                o.l = true;
                return o.exports;
            }

            n.m = t;
            n.c = e;
            n.d = function (t, e, r) {
                if (!n.o(t, e)) {
                    Object.defineProperty(t, e, {
                        enumerable: true,
                        get: r,
                    });
                }
            };
            n.r = function (t) {
                if (typeof Symbol !== "undefined" && Symbol.toStringTag) {
                    Object.defineProperty(t, Symbol.toStringTag, {
                        value: "Module",
                    });
                }
                Object.defineProperty(t, "__esModule", {
                    value: true,
                });
            };
            n.t = function (t, e) {
                if (e & 1) t = n(t);
                if (e & 8) return t;
                if (e & 4 && typeof t === "object" && t && t.__esModule) return t;
                var r = Object.create(null);
                n.r(r);
                Object.defineProperty(r, "default", {
                    enumerable: true,
                    value: t,
                });
                if (e & 2 && typeof t !== "string") {
                    for (var o in t) {
                        n.d(r, o, function (e) {
                            return t[e];
                        }.bind(null, o));
                    }
                }
                return r;
            };
            n.n = function (t) {
                var e =
                    t && t.__esModule
                        ? function () {
                              return t.default;
                          }
                        : function () {
                              return t;
                          };
                n.d(e, "a", e);
                return e;
            };
            n.o = function (t, e) {
                return Object.prototype.hasOwnProperty.call(t, e);
            };
            n.p = "";

            return n((n.s = 18));
        }([
            function (t, e, n) {
                function r(t) {
                    if (t) {
                        return (function (t) {
                            for (var e in r.prototype) {
                                t[e] = r.prototype[e];
                            }
                            return t;
                        })(t);
                    }
                }

                t.exports = r;

                r.prototype.on = r.prototype.addEventListener = function (t, e) {
                    this._callbacks = this._callbacks || {};
                    (this._callbacks["$" + t] = this._callbacks["$" + t] || []).push(e);
                    return this;
                };

                r.prototype.once = function (t, e) {
                    function n() {
                        this.off(t, n);
                        e.apply(this, arguments);
                    }
                    n.fn = e;
                    this.on(t, n);
                    return this;
                };

                r.prototype.off =
                    r.prototype.removeListener =
                    r.prototype.removeAllListeners =
                    r.prototype.removeEventListener =
                        function (t, e) {
                            this._callbacks = this._callbacks || {};
                            if (arguments.length === 0) {
                                this._callbacks = {};
                                return this;
                            }
                            var n,
                                r = this._callbacks["$" + t];
                            if (!r) return this;
                            if (arguments.length === 1) {
                                delete this._callbacks["$" + t];
                                return this;
                            }
                            for (var o = 0; o < r.length; o++) {
                                if ((n = r[o]) === e || n.fn === e) {
                                    r.splice(o, 1);
                                    break;
                                }
                            }
                            if (r.length === 0) {
                                delete this._callbacks["$" + t];
                            }
                            return this;
                        };

                r.prototype.emit = function (t) {
                    this._callbacks = this._callbacks || {};
                    var e = new Array(arguments.length - 1),
                        n = this._callbacks["$" + t];
                    for (var r = 1; r < arguments.length; r++) {
                        e[r - 1] = arguments[r];
                    }
                    if (n) {
                        n = n.slice(0);
                        for (var o = 0; o < n.length; ++o) {
                            n[o].apply(this, e);
                        }
                    }
                    return this;
                };
            },
        ]);
    }
);