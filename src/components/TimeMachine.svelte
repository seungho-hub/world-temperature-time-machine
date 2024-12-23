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
	<div class="body">
		<p class = "help"> 오른쪽 지도에서 국가를 선택할 수 있습니다! </p>
		<div class="prompt">
				<span>{countryInfo.name}의 </span>
				<input type="number" name="year" id="" />
				<span>년 후에 표면 온도 증가는 어느정도일까요?</span>
		</div>
		<div class="prediction">
			
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

		.body {
			padding: 30px;
			display : flex;
			flex-direction: column;
			gap : 20px;
			input {
				background: none;
				background-color: black;
				padding: 10px 10px;
				color: #ffffff;

				&:focus{
					outline : none;
				}
			}
		}
	}
</style>
