<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import AuthPage from "./routes/authorization/AuthPage.svelte";
  import RegisterPage from "./routes/authorization/RegisterPage.svelte";
  import HomePage from "./routes/home/homePage.svelte";
  import ChatPage from "./routes/test/ChatPage.svelte";
</script>

<Router>
  <Route path="/" component={HomePage} />
  <Route path="/auth" component={AuthPage} />
  <Route path="/register" component={RegisterPage} />
  <Route path="/test/chat" component={ChatPage} />
</Router>