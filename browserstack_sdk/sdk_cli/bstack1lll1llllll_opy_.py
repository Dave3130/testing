# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import bstack1llllll1111_opy_
from browserstack_sdk.sdk_cli.bstack11111111ll_opy_ import (
    bstack1lllllll11l_opy_,
    bstack1llll1l11l1_opy_,
    bstack1lll111llll_opy_,
    bstack1lllll111ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lllll1_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll111_opy_ import bstack1llll111l1l_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import bstack1llllll1111_opy_
import weakref
class bstack1lll11lll1l_opy_(bstack1llllll1111_opy_):
    bstack1lll1llll1l_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1lllll111ll_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1lllll111ll_opy_]]
    def __init__(self, bstack1lll1llll1l_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1llll1ll_opy_ = dict()
        self.bstack1lll1llll1l_opy_ = bstack1lll1llll1l_opy_
        self.frameworks = frameworks
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1lllllll111_opy_, bstack1llll1l11l1_opy_.POST), self.__1lll11111l1_opy_)
        if any(bstack1llll1lll1l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1llll1lll1l_opy_.bstack1llll1l1l11_opy_(
                (bstack1lllllll11l_opy_.bstack1111111l11_opy_, bstack1llll1l11l1_opy_.PRE), self.__1ll1lllll11_opy_
            )
            bstack1llll1lll1l_opy_.bstack1llll1l1l11_opy_(
                (bstack1lllllll11l_opy_.QUIT, bstack1llll1l11l1_opy_.POST), self.__1ll1llllll1_opy_
            )
    def __1lll11111l1_opy_(
        self,
        f: bstack1lll11llll1_opy_,
        bstack1ll1lllll1l_opy_: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11l11l1_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤᇆ"):
                return
            contexts = bstack1ll1lllll1l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11l11l1_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᇇ") in page.url:
                                self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡖࡸࡴࡸࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠦᇈ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111llll_opy_.bstack1llllllllll_opy_(instance, self.bstack1lll1llll1l_opy_, True)
                                self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡲࡤ࡫ࡪࡥࡩ࡯࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᇉ") + str(instance.ref()) + bstack11l11l1_opy_ (u"ࠦࠧᇊ"))
        except Exception as e:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡳࡥ࡬࡫ࠠ࠻ࠤᇋ"),e)
    def __1ll1lllll11_opy_(
        self,
        f: bstack1llll1lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111llll_opy_.get_state(instance, self.bstack1lll1llll1l_opy_, False):
            return
        if not f.bstack1lll111111l_opy_(f.hub_url(driver)):
            self.bstack1ll1llll1ll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111llll_opy_.bstack1llllllllll_opy_(instance, self.bstack1lll1llll1l_opy_, True)
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡩ࡯࡫ࡷ࠾ࠥࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᇌ") + str(instance.ref()) + bstack11l11l1_opy_ (u"ࠢࠣᇍ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111llll_opy_.bstack1llllllllll_opy_(instance, self.bstack1lll1llll1l_opy_, True)
        self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᇎ") + str(instance.ref()) + bstack11l11l1_opy_ (u"ࠤࠥᇏ"))
    def __1ll1llllll1_opy_(
        self,
        f: bstack1llll1lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1lllllll_opy_(instance)
        self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡵࡺ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᇐ") + str(instance.ref()) + bstack11l11l1_opy_ (u"ࠦࠧᇑ"))
    def bstack1lll1l1ll1l_opy_(self, context: bstack1llll111l1l_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllll111ll_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1llll11l_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1llll1lll1l_opy_.bstack1lll1111ll1_opy_(data[1])
                    and data[1].bstack1ll1llll11l_opy_(context)
                    and getattr(data[0](), bstack11l11l1_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᇒ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll1111111_opy_, reverse=reverse)
    def bstack1lll1ll111l_opy_(self, context: bstack1llll111l1l_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllll111ll_opy_]]:
        matches = []
        for data in self.bstack1ll1llll1ll_opy_.values():
            if (
                data[1].bstack1ll1llll11l_opy_(context)
                and getattr(data[0](), bstack11l11l1_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᇓ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll1111111_opy_, reverse=reverse)
    def bstack1ll1llll1l1_opy_(self, instance: bstack1lllll111ll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1lllllll_opy_(self, instance: bstack1lllll111ll_opy_) -> bool:
        if self.bstack1ll1llll1l1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111llll_opy_.bstack1llllllllll_opy_(instance, self.bstack1lll1llll1l_opy_, False)
            return True
        return False