from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class EnlighenmentProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Enlightenment', ProfileType.WindowMgr, description='')

	@property
	def packages(self) -> list[str]:
		return [
			"enlightenment",
			"terminology"
		]

	@property
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Lightdm