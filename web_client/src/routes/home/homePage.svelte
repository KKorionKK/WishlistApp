<script lang="ts">
    import Header from "../../components/Header.svelte";
    import Basement from "../../components/Basement.svelte";
    function test() {
        window.location.href = "/register"
    }
</script>

<Header></Header>
<div class="bodyDiv">
    <div class="content">
        <div class="content-headers">
            <h1>For everyone. For everything.</h1>
        </div>
        <div class="content-describe">
            <div class="sentence">
                <span style="color: #FF6B3D; font-weight: 700;">Track your wishilsts.</span>
                <span style="color: #C5C6BD;">Append and delete, add links and more. Append and delete, add links and more. Append and delete, add links and more.</span>
            </div>
            <div class="sentence">
                <span style="color: #FF6B3D; font-weight: 700;">Track your wishilsts.</span>
                <span style="color: #C5C6BD;">Append and delete, add links and more. Append and delete, add links and more. Append and delete, add links and more.</span>
            </div>
            <div class="sentence">
                <span style="color: #FF6B3D; font-weight: 700;">Track your wishilsts.</span>
                <span style="color: #C5C6BD;">Append and delete, add links and more. Append and delete, add links and more. Append and delete, add links and more.</span>
            </div>
            <div class="sentence">
                <span style="color: #FF6B3D; font-weight: 700;">Track your wishilsts.</span>
                <span style="color: #C5C6BD;">Append and delete, add links and more. Append and delete, add links and more. Append and delete, add links and more.</span>
            </div>
        </div>
    </div>
    <Basement></Basement>
</div>

<style>
    .bodyDiv {
       display: flex;
       flex-direction: column; 
    }
    .content {
        position: relative;
        margin-top: 50px;
        margin-left: 3em;
    }
    .content-headers {
        display: flex;
        flex-direction: column;
        justify-content: left;
        text-align: start;
        font-size: 5.2em;
        line-height: 1;
        color: #FF6B3D;
        user-select: none;
    }
    .content-describe {
        display: flex;
        flex-direction: row;
    }
    .sentence {
        flex: 1;
        display: inline-flexbox;
        text-align: start;
    }
</style>