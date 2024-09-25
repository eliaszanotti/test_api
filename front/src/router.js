import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store/authStore';

const HomePage = () => import('./components/home/HomePage.vue');
const PersonnalPage = () => import('./components/personnal/PersonnalPage.vue');
const CustomizePage = () => import('./components/customize/CustomizePage.vue');
const TitlePage = () => import('./components/title/TitlePage.vue');
const LangPage = () => import('./components/lang/LangPage.vue');
const ExperiencePage = () => import('./components/experience/ExperiencePage.vue');
const FormationPage = () => import('./components/formation/FormationPage.vue');
const HobbiePage = () => import('./components/hobbie/HobbiePage.vue');
const DownloadPage = () => import('./components/download/DownloadPage.vue');
const LoginPage = () => import('./components/auth/LoginPage.vue');
const LogoutPage = () => import('./components/auth/LogoutPage.vue');
const ProfilePage = () => import('./components/auth/ProfilePage.vue');

const routes = [
	{
		path: '/',
		component: HomePage,
	},
	{
		path: '/personnal',
		component: PersonnalPage,
		meta: { requiresAuth: true },
	},
	{
		path: '/customize',
		component: CustomizePage,
		meta: { requiresAuth: true },
	},
	{
		path: '/title',
		component: TitlePage,
		meta: { requiresAuth: true },
	},
	{
		path: '/lang',
		component: LangPage,
		meta: { requiresAuth: true },
	},
	{
		path: '/experience',
		component: ExperiencePage,
		meta: { requiresAuth: true },
	},
	{
		path: '/formation',
		component: FormationPage,
		meta: { requiresAuth: true },
	},
	{
		path: '/hobbie',
		component: HobbiePage,
		meta: { requiresAuth: true },
	},
	{
		path: '/download',
		component: DownloadPage,
		meta: { requiresAuth: true },
	},
	{
		path: '/login',
		component: LoginPage
	},
	{
		path: '/logout',
		component: LogoutPage,
	},
	{
		path: '/profile',
		component: ProfilePage,
		meta: { requiresAuth: true },
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

router.beforeEach((to, from, next) => {
	const authStore = useAuthStore();
	if (to.meta.requiresAuth && !authStore.isLogged) {
		next('/login');
	} else {
		next();
	}
});

export default router;