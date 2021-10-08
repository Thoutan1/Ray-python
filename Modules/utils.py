import hikari

async def loading_embed() -> hikari.Embed:
	loading_embed = hikari.Embed(description = "Loading...")
	return loading_embed
