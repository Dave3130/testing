# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1lll111ll11_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll1l11ll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1lll1l111l1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
import weakref
class bstack1llll11111l_opy_(bstack1111111ll1_opy_):
    bstack1llll11l11l_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llllllll1l_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llllllll1l_opy_]]
    def __init__(self, bstack1llll11l11l_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll11111l1_opy_ = dict()
        self.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
        self.frameworks = frameworks
        bstack1lll1l11ll1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_, bstack1llll1ll111_opy_.POST), self.__1lll1111lll_opy_)
        if any(bstack1lllll111l1_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll111l1_opy_.bstack1llllll1111_opy_(
                (bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.PRE), self.__1lll111111l_opy_
            )
            bstack1lllll111l1_opy_.bstack1llllll1111_opy_(
                (bstack1llll1lll11_opy_.QUIT, bstack1llll1ll111_opy_.POST), self.__1lll11111ll_opy_
            )
    def __1lll1111lll_opy_(
        self,
        f: bstack1lll1l11ll1_opy_,
        bstack1lll1111l1l_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1l1lll1_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦᆬ"):
                return
            contexts = bstack1lll1111l1l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1l1lll1_opy_ (u"ࠥࡥࡧࡵࡵࡵ࠼ࡥࡰࡦࡴ࡫ࠣᆭ") in page.url:
                                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡘࡺ࡯ࡳ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡱࡩࡼࠦࡰࡢࡩࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠨᆮ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, self.bstack1llll11l11l_opy_, True)
                                self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡴࡦ࡭ࡥࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᆯ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠨࠢᆰ"))
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࠽ࠦᆱ"),e)
    def __1lll111111l_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111ll11_opy_.get_state(instance, self.bstack1llll11l11l_opy_, False):
            return
        if not f.bstack1lll111l111_opy_(f.hub_url(driver)):
            self.bstack1lll11111l1_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, self.bstack1llll11l11l_opy_, True)
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᆲ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠤࠥᆳ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, self.bstack1llll11l11l_opy_, True)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡭ࡳ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᆴ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠦࠧᆵ"))
    def __1lll11111ll_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll1111l11_opy_(instance)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡷࡵࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᆶ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠨࠢᆷ"))
    def bstack1llll111ll1_opy_(self, context: bstack1lll1l111l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllllll1l_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll1111111_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll111l1_opy_.bstack1lll111llll_opy_(data[1])
                    and data[1].bstack1lll1111111_opy_(context)
                    and getattr(data[0](), bstack1l1lll1_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᆸ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll1111ll1_opy_, reverse=reverse)
    def bstack1llll11ll1l_opy_(self, context: bstack1lll1l111l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllllll1l_opy_]]:
        matches = []
        for data in self.bstack1lll11111l1_opy_.values():
            if (
                data[1].bstack1lll1111111_opy_(context)
                and getattr(data[0](), bstack1l1lll1_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᆹ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll1111ll1_opy_, reverse=reverse)
    def bstack1ll1lllllll_opy_(self, instance: bstack1llllllll1l_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll1111l11_opy_(self, instance: bstack1llllllll1l_opy_) -> bool:
        if self.bstack1ll1lllllll_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, self.bstack1llll11l11l_opy_, False)
            return True
        return False