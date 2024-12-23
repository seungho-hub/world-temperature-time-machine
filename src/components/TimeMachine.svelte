<script lang="ts">
	import { slide } from 'svelte/transition';
	const { cc } = $props();

	const regionNames = new Intl.DisplayNames(['en'], { type: 'region' });

	function generateFlagImageUrl(cc: string) {
		return `https://flagcdn.com/48x36/${cc}.png`;
	}

	interface CountryInfo {
		cc?: string;
		name?: string;
		flagImageUrl?: string;
	}

	let countryInfo: CountryInfo = $state({
		cc: '',
		name: '',
		flagImageUrl: ''
	});

	$effect(() => {
		countryInfo = {
			cc,
			name: regionNames.of(cc.toUpperCase()),
			flagImageUrl: generateFlagImageUrl(cc)
		};
	});
</script>

<section transition:slide class="time-machine">
	<div class="header">
		<div class="country-flag">
			<img src={countryInfo.flagImageUrl} alt="" />
		</div>
		<div class="country-name">
			<h2>{countryInfo.name}</h2>
		</div>
	</div>
</section>

<style lang="scss">
	section.time-machine {
		height: 100%;
		width: 600px;
		padding: 40px 20px;
		border-right: 1px solid rgba(255, 255, 255, 0.3);
		display: flex;
		flex-direction: column;
		align-items: center;
		.header {
			display: flex;
			flex-direction: row;
			gap: 20px;
			img {
				width: 40px;
			}
		}
	}
</style>
