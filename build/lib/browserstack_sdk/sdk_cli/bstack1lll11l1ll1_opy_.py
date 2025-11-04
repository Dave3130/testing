# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
from browserstack_sdk.sdk_cli.bstack1llll111l1l_opy_ import bstack1llll1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111l1_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack1lllll11ll1_opy_,
    bstack1lll111l11l_opy_,
    bstack1llll1ll11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1llllll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll11ll_opy_ import bstack1llll1111l1_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll111l1l_opy_ import bstack1llll1l1ll1_opy_
import weakref
class bstack1lll1ll1l1l_opy_(bstack1llll1l1ll1_opy_):
    bstack1lll1l1ll11_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llll1ll11l_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llll1ll11l_opy_]]
    def __init__(self, bstack1lll1l1ll11_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1llll1ll_opy_ = dict()
        self.bstack1lll1l1ll11_opy_ = bstack1lll1l1ll11_opy_
        self.frameworks = frameworks
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_, bstack1lllll11ll1_opy_.POST), self.__1ll1llll11l_opy_)
        if any(bstack1lllll11111_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll11111_opy_.bstack1llllll11l1_opy_(
                (bstack1lllllll1ll_opy_.bstack1llll1l1l1l_opy_, bstack1lllll11ll1_opy_.PRE), self.__1ll1llll111_opy_
            )
            bstack1lllll11111_opy_.bstack1llllll11l1_opy_(
                (bstack1lllllll1ll_opy_.QUIT, bstack1lllll11ll1_opy_.POST), self.__1ll1lll1l11_opy_
            )
    def __1ll1llll11l_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        bstack1ll1llll1l1_opy_: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11l1111_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦᇤ"):
                return
            contexts = bstack1ll1llll1l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack11l1111_opy_ (u"ࠥࡥࡧࡵࡵࡵ࠼ࡥࡰࡦࡴ࡫ࠣᇥ") in page.url:
                                self.logger.debug(bstack11l1111_opy_ (u"ࠦࡘࡺ࡯ࡳ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡱࡩࡼࠦࡰࡢࡩࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠨᇦ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111l11l_opy_.bstack1llllll1111_opy_(instance, self.bstack1lll1l1ll11_opy_, True)
                                self.logger.debug(bstack11l1111_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡴࡦ࡭ࡥࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᇧ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠨࠢᇨ"))
        except Exception as e:
            self.logger.debug(bstack11l1111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࠽ࠦᇩ"),e)
    def __1ll1llll111_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111l11l_opy_.get_state(instance, self.bstack1lll1l1ll11_opy_, False):
            return
        if not f.bstack1ll1lll111l_opy_(f.hub_url(driver)):
            self.bstack1ll1llll1ll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111l11l_opy_.bstack1llllll1111_opy_(instance, self.bstack1lll1l1ll11_opy_, True)
            self.logger.debug(bstack11l1111_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᇪ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠤࠥᇫ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111l11l_opy_.bstack1llllll1111_opy_(instance, self.bstack1lll1l1ll11_opy_, True)
        self.logger.debug(bstack11l1111_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡭ࡳ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᇬ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠦࠧᇭ"))
    def __1ll1lll1l11_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1lll1ll1_opy_(instance)
        self.logger.debug(bstack11l1111_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡷࡵࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᇮ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠨࠢᇯ"))
    def bstack1lll1lll1l1_opy_(self, context: bstack1llll1111l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1ll11l_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1lll11l1_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll11111_opy_.bstack1lll1111111_opy_(data[1])
                    and data[1].bstack1ll1lll11l1_opy_(context)
                    and getattr(data[0](), bstack11l1111_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᇰ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lll1lll_opy_, reverse=reverse)
    def bstack1lll1l111l1_opy_(self, context: bstack1llll1111l1_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1ll11l_opy_]]:
        matches = []
        for data in self.bstack1ll1llll1ll_opy_.values():
            if (
                data[1].bstack1ll1lll11l1_opy_(context)
                and getattr(data[0](), bstack11l1111_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᇱ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lll1lll_opy_, reverse=reverse)
    def bstack1ll1lll1l1l_opy_(self, instance: bstack1llll1ll11l_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1lll1ll1_opy_(self, instance: bstack1llll1ll11l_opy_) -> bool:
        if self.bstack1ll1lll1l1l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111l11l_opy_.bstack1llllll1111_opy_(instance, self.bstack1lll1l1ll11_opy_, False)
            return True
        return False