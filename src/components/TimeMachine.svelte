<script lang="ts">
	import image0 from '$lib/assets/0.webp';
	import image1 from '$lib/assets/1.webp';
	import image2 from '$lib/assets/2.webp';
	import image3 from '$lib/assets/3.webp';
	import image4 from '$lib/assets/4.webp';
	import image5 from '$lib/assets/5.webp';
	import image6 from '$lib/assets/6.webp';

	import { slide } from 'svelte/transition';
	const { cc } = $props();

	const regionNames = new Intl.DisplayNames(['en'], { type: 'region' });

	function generateFlagImageUrl(cc: string) {
		return `https://flagcdn.com/48x36/${cc}.png`;
	}

	interface CountryInfo {
		cc: string;
		name: string;
		flagImageUrl: string;
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

		year = 2024;
		prediction = 0;
	});

	let year = 2024;

	let prediction = $state(0);

	let loading = $state(false);
	function fetchPrediction() {
		loading = true;
		fetch(`/api/predict?cc=${cc}&year=${year}`)
			.then((res) => res.json())
			.then((data) => {
				prediction = parseFloat(data.prediction).toFixed(2);
				loading = false;
			});
	}
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
		<p class="help">오른쪽 지도에서 국가를 선택할 수 있습니다!</p>
		<div class="prompt">
			<span
				>{countryInfo.name}의
				<form action="" on:submit={fetchPrediction}>
					<input type="number" name="year" id="" bind:value={year} min="1960" />
				</form></span
			>

			<span>년에는 표면 온도가 어느정도 증가할까요?</span>
		</div>
		<div class="prediction">
			{#if loading}
				<span class="loader"></span>
			{:else if prediction}
				<p>{prediction} °C 상승할 예정입니다</p>
				<div class="description">
					<ul>
						{#if prediction < 1}
							<img src={image0} />
							<p>평범한 지구입니다</p>
						{:else if prediction > 1 && prediction < 2}
							<img src={image1} />
							<li>
								북극 해빙 면적의 현저한 감소가 시작되며, 여름철 북극이 얼음 없는 상태에 가까워짐
							</li>
							<li>
								열 팽창과 빙하 융해로 인해 해수면이 상승, 저지대 해안 도시들이 홍수 위험에 직면
							</li>
							<li>산호초의 70~90%가 손상되거나 백화됨</li>
							<li>더 잦은 폭염, 폭우, 가뭄 등 이상 기후 현상이 발생</li>
						{:else if prediction > 2 && prediction < 3}
							<img src={image2} />
							<li>그린란드와 서남극의 빙하가 불안정해지며 더 빠른 융해가 진행됨</li>
							<li>
								전 세계 생물 종의 18%가 멸종 위기에 처함 특히, 북극곰과 같은 극지 생물이 서식지를
								잃음
							</li>
							<li>곡물 생산량이 급격히 감소하며, 세계 식량 안보가 위협받음</li>
							<li>허리케인, 태풍 등의 빈도와 강도가 증가</li>
						{:else if prediction > 3 && prediction < 4}
							<img src={image3} />
							<li>해수면이 최대 1m 이상 상승, 수백만 명의 사람들이 해안 지역에서 대규모 이주</li>
							<li>주요 농업 지역이 사막화되며, 물 부족 문제가 심화됨</li>
							<li>홍수, 산불, 열파(heat wave)의 빈도와 강도가 크게 증가</li>
							<li>열 관련 사망자 수 증가, 전염병(예: 말라리아, 뎅기열) 확산</li>
						{:else if prediction > 4 && prediction < 5}
							<img src={image4} />
							<li>영구동토층에서 메탄 방출이 가속화되어 온난화를 더욱 심화시킴</li>
							<li>해양 순환이 중단되며, 전 세계 기후가 더욱 불안정</li>
							<li>식수와 식량 부족으로 인해 대규모 기근이 발생</li>
							<li>수억 명의 기후 난민이 생겨남</li>
							<li>주요 도시가 침수될 위험에 처함</li>
						{:else if prediction > 5 && prediction < 10}
							<img src={image5} />
							<li>지구상의 대부분의 생태계가 기능을 상실하며 대멸종 사태가 발생</li>
							<li>인간이 거주 가능한 지역이 거의 사라짐</li>
							<li>경제 시스템 붕괴, 사회적 갈등과 전쟁이 빈번히 발생</li>
						{:else}
							<img src={image6} />
							<p>이런! 지구에 더이상 사람이 없네요!</p>
						{/if}
					</ul>
				</div>
			{:else}
				연도를 입력하고 결과를 확인해보세요!
			{/if}
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
			display: flex;
			flex-direction: column;
			gap: 20px;

			form {
				display: inline;
				input {
					background: none;
					background-color: black;
					padding: 10px 10px;
					color: #ffffff;

					&:focus {
						outline: none;
					}
				}
			}

			.prediction {
				display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: center;
				gap: 20px;
				height: auto;
				min-height: 200px;
				.description {
					padding: 20px;
					img {
						width: 200px;
						margin-bottom: 20px;
					}
					ul {
						gap: 10px;
						li {
							margin: 10px;
						}
					}
				}
			}
		}
	}

	.loader {
		font-size: 10px;
		width: 1em;
		height: 1em;
		border-radius: 50%;
		position: relative;
		text-indent: -9999em;
		animation: mulShdSpin 1.1s infinite ease;
		transform: translateZ(0);
	}
	@keyframes mulShdSpin {
		0%,
		100% {
			box-shadow:
				0em -2.6em 0em 0em #ffffff,
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2),
				2.5em 0em 0 0em rgba(255, 255, 255, 0.2),
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2),
				0em 2.5em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2),
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.5),
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.7);
		}
		12.5% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.7),
				1.8em -1.8em 0 0em #ffffff,
				2.5em 0em 0 0em rgba(255, 255, 255, 0.2),
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2),
				0em 2.5em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2),
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.5);
		}
		25% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.5),
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.7),
				2.5em 0em 0 0em #ffffff,
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2),
				0em 2.5em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2),
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
		}
		37.5% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.2),
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.5),
				2.5em 0em 0 0em rgba(255, 255, 255, 0.7),
				1.75em 1.75em 0 0em #ffffff,
				0em 2.5em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2),
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
		}
		50% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.2),
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2),
				2.5em 0em 0 0em rgba(255, 255, 255, 0.5),
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.7),
				0em 2.5em 0 0em #ffffff,
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2),
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
		}
		62.5% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.2),
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2),
				2.5em 0em 0 0em rgba(255, 255, 255, 0.2),
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.5),
				0em 2.5em 0 0em rgba(255, 255, 255, 0.7),
				-1.8em 1.8em 0 0em #ffffff,
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
		}
		75% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.2),
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2),
				2.5em 0em 0 0em rgba(255, 255, 255, 0.2),
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2),
				0em 2.5em 0 0em rgba(255, 255, 255, 0.5),
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.7),
				-2.6em 0em 0 0em #ffffff,
				-1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
		}
		87.5% {
			box-shadow:
				0em -2.6em 0em 0em rgba(255, 255, 255, 0.2),
				1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2),
				2.5em 0em 0 0em rgba(255, 255, 255, 0.2),
				1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2),
				0em 2.5em 0 0em rgba(255, 255, 255, 0.2),
				-1.8em 1.8em 0 0em rgba(255, 255, 255, 0.5),
				-2.6em 0em 0 0em rgba(255, 255, 255, 0.7),
				-1.8em -1.8em 0 0em #ffffff;
		}
	}
</style>
