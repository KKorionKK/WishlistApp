<script lang="ts">
    export let data: string, owner: boolean;
</script>

<div>
   {#if owner}
   <span>Вы: {data}</span>
   {:else}
   <span>Cервер: {data}</span>
   {/if}
</div>

<style>
    div {
        display: flex;
        flex-direction: row;
    }
    span {
        left: 0;
    }
</style>