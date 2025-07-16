import { componentStore } from "routelit-client";
import './lib.css'
import {
  Hello,
} from "./components";

componentStore.register("hello", Hello);
componentStore.forceUpdate();
