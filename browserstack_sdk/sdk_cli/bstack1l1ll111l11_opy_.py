# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1llll1l1111_opy_,
)
from bstack_utils.helper import  bstack1l1lll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1lll_opy_, bstack1lll1l1ll1l_opy_, bstack1lll11lll1l_opy_, bstack1ll11ll1l1l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11l11l11l1_opy_ import bstack11lllll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll111ll1l_opy_
from bstack_utils.percy import bstack1l11ll1ll1_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l11l11ll_opy_(bstack1llll1l1l11_opy_):
    def __init__(self, bstack11lllll1l11_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll1l11_opy_ = bstack11lllll1l11_opy_
        self.percy = bstack1l11ll1ll1_opy_()
        self.bstack11l1llll1_opy_ = bstack11lllll1ll_opy_()
        self.bstack11llll1lll1_opy_()
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack11lllll1lll_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1llll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l111lll111_opy_(self, instance: bstack1llll1l1111_opy_, driver: object):
        bstack1l11l11ll1l_opy_ = TestFramework.bstack1l111lll1l1_opy_(instance.context)
        for t in bstack1l11l11ll1l_opy_:
            bstack1lll111l1ll_opy_ = TestFramework.get_state(t, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l1ll_opy_) or instance == driver:
                return t
    def bstack11lllll1lll_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll11l1l_opy_.bstack1l1ll1lllll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_, 0)
            bstack1ll111llll1_opy_ = self.bstack1l111lll111_opy_(instance, driver)
            bstack11lllll1l1l_opy_ = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1l1llll1l11_opy_, None)
            if not bstack11lllll1l1l_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡲࡦࡶࡸࡶࡳ࡯࡮ࡨࠢࡤࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡩࡴࠢࡱࡳࡹࠦࡹࡦࡶࠣࡷࡹࡧࡲࡵࡧࡧࠦᔼ"))
                return
            driver_command = f.bstack1l1lll1111l_opy_(*args)
            for command in bstack11l11111ll_opy_:
                if command == driver_command:
                    self.bstack11l1l1ll1l_opy_(driver, platform_index)
            bstack1ll1l1l1l_opy_ = self.percy.bstack1l1l1l111l_opy_()
            if driver_command in bstack1lll111111_opy_[bstack1ll1l1l1l_opy_]:
                self.bstack11l1llll1_opy_.bstack11ll1l1l1l_opy_(bstack11lllll1l1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡦࡴࡵࡳࡷࠨᔽ"), e)
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
        bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᔾ") + str(kwargs) + bstack11l111_opy_ (u"ࠢࠣᔿ"))
            return
        if len(bstack1lll111l1ll_opy_) > 1:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕀ") + str(kwargs) + bstack11l111_opy_ (u"ࠤࠥᕁ"))
        bstack1lll11111ll_opy_, bstack1lll1llllll_opy_ = bstack1lll111l1ll_opy_[0]
        driver = bstack1lll11111ll_opy_()
        if not driver:
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᕂ") + str(kwargs) + bstack11l111_opy_ (u"ࠦࠧᕃ"))
            return
        bstack11lllll1111_opy_ = {
            TestFramework.bstack1ll1l11l111_opy_: bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᕄ"),
            TestFramework.bstack1lll1lll1l1_opy_: bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᕅ"),
            TestFramework.bstack1l1llll1l11_opy_: bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࠥࡸࡥࡳࡷࡱࠤࡳࡧ࡭ࡦࠤᕆ")
        }
        bstack11llll1llll_opy_ = { key: f.get_state(instance, key) for key in bstack11lllll1111_opy_ }
        bstack11lllll11l1_opy_ = [key for key, value in bstack11llll1llll_opy_.items() if not value]
        if bstack11lllll11l1_opy_:
            for key in bstack11lllll11l1_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠦᕇ") + str(key) + bstack11l111_opy_ (u"ࠤࠥᕈ"))
            return
        platform_index = f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_, 0)
        if self.bstack11lllll1l11_opy_.percy_capture_mode == bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧᕉ"):
            bstack11lll1l1ll_opy_ = bstack11llll1llll_opy_.get(TestFramework.bstack1l1llll1l11_opy_) + bstack11l111_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕊ")
            bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack11lllll1ll1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11lll1l1ll_opy_,
                bstack1111l1ll11_opy_=bstack11llll1llll_opy_[TestFramework.bstack1ll1l11l111_opy_],
                bstack1lll11ll11_opy_=bstack11llll1llll_opy_[TestFramework.bstack1lll1lll1l1_opy_],
                bstack1ll1l1l11_opy_=platform_index
            )
            bstack1llll11ll11_opy_.end(EVENTS.bstack11lllll1ll1_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᕋ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᕌ"), True, None, None, None, None, test_name=bstack11lll1l1ll_opy_)
    def bstack11l1l1ll1l_opy_(self, driver, platform_index):
        if self.bstack11l1llll1_opy_.bstack111l1ll11l_opy_() is True or self.bstack11l1llll1_opy_.capturing() is True:
            return
        self.bstack11l1llll1_opy_.bstack11ll111l11_opy_()
        while not self.bstack11l1llll1_opy_.bstack111l1ll11l_opy_():
            bstack11lllll1l1l_opy_ = self.bstack11l1llll1_opy_.bstack111l1l1l11_opy_()
            self.bstack1l1lll1ll_opy_(driver, bstack11lllll1l1l_opy_, platform_index)
        self.bstack11l1llll1_opy_.bstack111l1l1111_opy_()
    def bstack1l1lll1ll_opy_(self, driver, bstack11ll1ll1l_opy_, platform_index, test=None):
        from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
        bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack111lll1ll1_opy_.value)
        if test != None:
            bstack1111l1ll11_opy_ = getattr(test, bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᕍ"), None)
            bstack1lll11ll11_opy_ = getattr(test, bstack11l111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᕎ"), None)
            PercySDK.screenshot(driver, bstack11ll1ll1l_opy_, bstack1111l1ll11_opy_=bstack1111l1ll11_opy_, bstack1lll11ll11_opy_=bstack1lll11ll11_opy_, bstack1ll1l1l11_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11ll1ll1l_opy_)
        bstack1llll11ll11_opy_.end(EVENTS.bstack111lll1ll1_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᕏ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᕐ"), True, None, None, None, None, test_name=bstack11ll1ll1l_opy_)
    def bstack11llll1lll1_opy_(self):
        os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᕑ")] = str(self.bstack11lllll1l11_opy_.success)
        os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩᕒ")] = str(self.bstack11lllll1l11_opy_.percy_capture_mode)
        self.percy.bstack11lllll111l_opy_(self.bstack11lllll1l11_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll11ll_opy_(self.bstack11lllll1l11_opy_.percy_build_id)