# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1lll11ll1l1_opy_,
    bstack1111111l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l1l_opy_ import bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1llll11l1l1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
import weakref
class bstack1lll1l1l111_opy_(bstack1llll1ll11l_opy_):
    bstack1lll1ll1lll_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1111111l11_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1111111l11_opy_]]
    def __init__(self, bstack1lll1ll1lll_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll1111l11_opy_ = dict()
        self.bstack1lll1ll1lll_opy_ = bstack1lll1ll1lll_opy_
        self.frameworks = frameworks
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_, bstack1lllll1lll1_opy_.POST), self.__1lll11111ll_opy_)
        if any(bstack1lllll1ll11_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll1ll11_opy_.bstack11111111ll_opy_(
                (bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.PRE), self.__1lll1111lll_opy_
            )
            bstack1lllll1ll11_opy_.bstack11111111ll_opy_(
                (bstack1llll1ll1ll_opy_.QUIT, bstack1lllll1lll1_opy_.POST), self.__1lll11111l1_opy_
            )
    def __1lll11111ll_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1lll111l1l1_opy_: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1lllll1_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤᆱ"):
                return
            contexts = bstack1lll111l1l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1lllll1_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᆲ") in page.url:
                                self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡖࡸࡴࡸࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠦᆳ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, self.bstack1lll1ll1lll_opy_, True)
                                self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡲࡤ࡫ࡪࡥࡩ࡯࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᆴ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠦࠧᆵ"))
        except Exception as e:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡳࡥ࡬࡫ࠠ࠻ࠤᆶ"),e)
    def __1lll1111lll_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll11ll1l1_opy_.get_state(instance, self.bstack1lll1ll1lll_opy_, False):
            return
        if not f.bstack1lll111l11l_opy_(f.hub_url(driver)):
            self.bstack1lll1111l11_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, self.bstack1lll1ll1lll_opy_, True)
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡩ࡯࡫ࡷ࠾ࠥࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᆷ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠢࠣᆸ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, self.bstack1lll1ll1lll_opy_, True)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᆹ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠤࠥᆺ"))
    def __1lll11111l1_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll1111l1l_opy_(instance)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡵࡺ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᆻ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠦࠧᆼ"))
    def bstack1lll1ll111l_opy_(self, context: bstack1llll11l1l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1111111l11_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll111111l_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll1ll11_opy_.bstack1lll11l1111_opy_(data[1])
                    and data[1].bstack1lll111111l_opy_(context)
                    and getattr(data[0](), bstack1lllll1_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᆽ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll111l111_opy_, reverse=reverse)
    def bstack1lll1l1ll1l_opy_(self, context: bstack1llll11l1l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1111111l11_opy_]]:
        matches = []
        for data in self.bstack1lll1111l11_opy_.values():
            if (
                data[1].bstack1lll111111l_opy_(context)
                and getattr(data[0](), bstack1lllll1_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᆾ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll111l111_opy_, reverse=reverse)
    def bstack1lll1111ll1_opy_(self, instance: bstack1111111l11_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll1111l1l_opy_(self, instance: bstack1111111l11_opy_) -> bool:
        if self.bstack1lll1111ll1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, self.bstack1lll1ll1lll_opy_, False)
            return True
        return False