<script lang="ts">
    import ServerMessage from "../../components/ServerMessage.svelte";
    import UserMessage from "../../components/UserMessage.svelte";

    let chat_id = Date.now()
    let ws = new WebSocket(`ws://localhost:8000/v1/chat/${chat_id}`);
    ws.onmessage = function(event) {
        let serverMessage = new ServerMessage({
            target: document.querySelector(".messagesBox"),
            props: {
                data: event.data,
                owner: false
            }
        });
    };
    function sendMessage() {
        let input: Element | null = document.querySelector(".inputText");
        ws.send(input?.value)

        let serverMessage = new UserMessage({
            target: document.querySelector(".messagesBox"),
            props: {
                data: input?.value,
            }
        });

        input.value = ''
        
    }
</script>

<form action="" on:submit|preventDefault={sendMessage}>
    <div class="chatBox">
        <div class="messagesBox">
        </div>
        <div class="controls">
            <input minlength="3" required type="text" class="inputText" placeholder="Your message">
            <input type="submit" class="sendBtn" value="Send">
        </div>
    </div>
</form>

<style>
    .chatBox {
        width: 400px;
        height: 500px;
        border: #FF6B3D solid 1px;
        border-radius: 30px;
        display: flex;
        flex-direction: column;
        padding: 30px
    }
    .messagesBox {
        flex: 1;
        overflow-y: scroll;
        padding: 20px;
    }
    .controls {
        display: flex;
        flex-direction: row;
    }
    .inputText {
        border: #FF6B3D solid 1px;
        flex: 4;
        background: none;
        border-radius: 10px;
        padding: 10px;
    }
    .sendBtn {
        padding: 10px;
        margin-left: 10px;
        text-align: center;
        border: none;
        flex: 1;
        cursor: pointer;
        background-color: #FF6B3D;
        border-radius: 10px;
        color: #F6F8EC;
    }
</style>