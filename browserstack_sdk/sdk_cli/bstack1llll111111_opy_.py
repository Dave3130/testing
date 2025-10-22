# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llllllllll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1llll1l1l1l_opy_,
    bstack1lllllll111_opy_,
    bstack1lll111ll11_opy_,
    bstack1llll11l1ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1lll1llllll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lllll1l_opy_ import bstack1lll1l1111l_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1llllllllll_opy_
import weakref
class bstack1lll1l1lll1_opy_(bstack1llllllllll_opy_):
    bstack1lll1l1l1l1_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llll11l1ll_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llll11l1ll_opy_]]
    def __init__(self, bstack1lll1l1l1l1_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1lll1l11_opy_ = dict()
        self.bstack1lll1l1l1l1_opy_ = bstack1lll1l1l1l1_opy_
        self.frameworks = frameworks
        bstack1lll1llllll_opy_.bstack1llll1ll1ll_opy_((bstack1llll1l1l1l_opy_.bstack1lllll1ll1l_opy_, bstack1lllllll111_opy_.POST), self.__1ll1llll11l_opy_)
        if any(bstack1lllllll11l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllllll11l_opy_.bstack1llll1ll1ll_opy_(
                (bstack1llll1l1l1l_opy_.bstack1lllll111ll_opy_, bstack1lllllll111_opy_.PRE), self.__1ll1llll1ll_opy_
            )
            bstack1lllllll11l_opy_.bstack1llll1ll1ll_opy_(
                (bstack1llll1l1l1l_opy_.QUIT, bstack1lllllll111_opy_.POST), self.__1ll1llll1l1_opy_
            )
    def __1ll1llll11l_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        bstack1llllll11l1_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11l1l11_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤᇍ"):
                return
            contexts = bstack1ll1llll111_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11l1l11_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᇎ") in page.url:
                                self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡖࡸࡴࡸࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠦᇏ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111ll11_opy_.bstack1llllll1l11_opy_(instance, self.bstack1lll1l1l1l1_opy_, True)
                                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡲࡤ࡫ࡪࡥࡩ࡯࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᇐ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠦࠧᇑ"))
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡳࡥ࡬࡫ࠠ࠻ࠤᇒ"),e)
    def __1ll1llll1ll_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        bstack1llllll11l1_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111ll11_opy_.get_state(instance, self.bstack1lll1l1l1l1_opy_, False):
            return
        if not f.bstack1ll1llllll1_opy_(f.hub_url(driver)):
            self.bstack1ll1lll1l11_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111ll11_opy_.bstack1llllll1l11_opy_(instance, self.bstack1lll1l1l1l1_opy_, True)
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡩ࡯࡫ࡷ࠾ࠥࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᇓ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠢࠣᇔ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111ll11_opy_.bstack1llllll1l11_opy_(instance, self.bstack1lll1l1l1l1_opy_, True)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᇕ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠤࠥᇖ"))
    def __1ll1llll1l1_opy_(
        self,
        f: bstack1lllllll11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l1ll_opy_, str],
        bstack1llllll11l1_opy_: Tuple[bstack1llll1l1l1l_opy_, bstack1lllllll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1lll1lll_opy_(instance)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡵࡺ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᇗ") + str(instance.ref()) + bstack11l1l11_opy_ (u"ࠦࠧᇘ"))
    def bstack1lll11lll11_opy_(self, context: bstack1lll1l1111l_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll11l1ll_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1lll1ll1_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllllll11l_opy_.bstack1lll11l1111_opy_(data[1])
                    and data[1].bstack1ll1lll1ll1_opy_(context)
                    and getattr(data[0](), bstack11l1l11_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᇙ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lll1l1l_opy_, reverse=reverse)
    def bstack1lll11llll1_opy_(self, context: bstack1lll1l1111l_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll11l1ll_opy_]]:
        matches = []
        for data in self.bstack1ll1lll1l11_opy_.values():
            if (
                data[1].bstack1ll1lll1ll1_opy_(context)
                and getattr(data[0](), bstack11l1l11_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᇚ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lll1l1l_opy_, reverse=reverse)
    def bstack1ll1lllll11_opy_(self, instance: bstack1llll11l1ll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1lll1lll_opy_(self, instance: bstack1llll11l1ll_opy_) -> bool:
        if self.bstack1ll1lllll11_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111ll11_opy_.bstack1llllll1l11_opy_(instance, self.bstack1lll1l1l1l1_opy_, False)
            return True
        return False