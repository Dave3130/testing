# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import (
    bstack1llll11llll_opy_,
    bstack1llll11l1l1_opy_,
    bstack1llll1l1l11_opy_,
)
from bstack_utils.helper import  bstack1lllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llll11ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1l11l_opy_, bstack1lll1l11lll_opy_, bstack1lll11lll1l_opy_, bstack1ll11lll11l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11ll11111_opy_ import bstack1l11l111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111lll_opy_ import bstack1lll11111l1_opy_
from bstack_utils.percy import bstack11lll11l11_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l11llll1_opy_(bstack1lllll1l111_opy_):
    def __init__(self, bstack11lllll11ll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll11ll_opy_ = bstack11lllll11ll_opy_
        self.percy = bstack11lll11l11_opy_()
        self.bstack1l11l1l11_opy_ = bstack1l11l111l1_opy_()
        self.bstack11llll1lll1_opy_()
        bstack1llll11ll11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_, bstack1llll11l1l1_opy_.PRE), self.bstack11lllll111l_opy_)
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1l11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1l1111_opy_(self, instance: bstack1llll1l1l11_opy_, driver: object):
        bstack1l11l11llll_opy_ = TestFramework.bstack1l111lll111_opy_(instance.context)
        for t in bstack1l11l11llll_opy_:
            bstack1lll111l1ll_opy_ = TestFramework.get_state(t, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l1ll_opy_) or instance == driver:
                return t
    def bstack11lllll111l_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll11ll11_opy_.bstack1l1ll1lll1l_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_, 0)
            bstack1ll11l1l1ll_opy_ = self.bstack1l11l1l1111_opy_(instance, driver)
            bstack11llll1ll11_opy_ = TestFramework.get_state(bstack1ll11l1l1ll_opy_, TestFramework.bstack1l1lll1llll_opy_, None)
            if not bstack11llll1ll11_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡸࡥࡵࡷࡵࡲ࡮ࡴࡧࠡࡣࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡯ࡳࠡࡰࡲࡸࠥࡿࡥࡵࠢࡶࡸࡦࡸࡴࡦࡦࠥᕉ"))
                return
            driver_command = f.bstack1l1ll1l1ll1_opy_(*args)
            for command in bstack11ll11ll1_opy_:
                if command == driver_command:
                    self.bstack1lll1l11ll_opy_(driver, platform_index)
            bstack11lll1lll1_opy_ = self.percy.bstack11l1l1111l_opy_()
            if driver_command in bstack11ll111ll1_opy_[bstack11lll1lll1_opy_]:
                self.bstack1l11l1l11_opy_.bstack11l111ll11_opy_(bstack11llll1ll11_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡥࡳࡴࡲࡶࠧᕊ"), e)
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
        bstack1lll111l1ll_opy_ = f.get_state(instance, bstack1lll11111l1_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕋ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠨࠢᕌ"))
            return
        if len(bstack1lll111l1ll_opy_) > 1:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᕍ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠣࠤᕎ"))
        bstack1ll1lllll1l_opy_, bstack1llll11111l_opy_ = bstack1lll111l1ll_opy_[0]
        driver = bstack1ll1lllll1l_opy_()
        if not driver:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕏ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠥࠦᕐ"))
            return
        bstack11llll1l1l1_opy_ = {
            TestFramework.bstack1ll11111l1l_opy_: bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᕑ"),
            TestFramework.bstack1lll1lllll1_opy_: bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᕒ"),
            TestFramework.bstack1l1lll1llll_opy_: bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࠤࡷ࡫ࡲࡶࡰࠣࡲࡦࡳࡥࠣᕓ")
        }
        bstack11llll1llll_opy_ = { key: f.get_state(instance, key) for key in bstack11llll1l1l1_opy_ }
        bstack11llll1l1ll_opy_ = [key for key, value in bstack11llll1llll_opy_.items() if not value]
        if bstack11llll1l1ll_opy_:
            for key in bstack11llll1l1ll_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠥᕔ") + str(key) + bstack11ll1l_opy_ (u"ࠣࠤᕕ"))
            return
        platform_index = f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_, 0)
        if self.bstack11lllll11ll_opy_.percy_capture_mode == bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᕖ"):
            bstack11ll1ll11l_opy_ = bstack11llll1llll_opy_.get(TestFramework.bstack1l1lll1llll_opy_) + bstack11ll1l_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᕗ")
            bstack1ll111l1l1l_opy_ = bstack1llll111ll1_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack11llll1ll1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11ll1ll11l_opy_,
                bstack11ll1llll_opy_=bstack11llll1llll_opy_[TestFramework.bstack1ll11111l1l_opy_],
                bstack1111111l1_opy_=bstack11llll1llll_opy_[TestFramework.bstack1lll1lllll1_opy_],
                bstack1ll1l11l1_opy_=platform_index
            )
            bstack1llll111ll1_opy_.end(EVENTS.bstack11llll1ll1l_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕘ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕙ"), True, None, None, None, None, test_name=bstack11ll1ll11l_opy_)
    def bstack1lll1l11ll_opy_(self, driver, platform_index):
        if self.bstack1l11l1l11_opy_.bstack1l1ll11l1_opy_() is True or self.bstack1l11l1l11_opy_.capturing() is True:
            return
        self.bstack1l11l1l11_opy_.bstack1l11l1l111_opy_()
        while not self.bstack1l11l1l11_opy_.bstack1l1ll11l1_opy_():
            bstack11llll1ll11_opy_ = self.bstack1l11l1l11_opy_.bstack11llll111l_opy_()
            self.bstack1lll1l1111_opy_(driver, bstack11llll1ll11_opy_, platform_index)
        self.bstack1l11l1l11_opy_.bstack11lll111l1_opy_()
    def bstack1lll1l1111_opy_(self, driver, bstack1l11l1l1ll_opy_, platform_index, test=None):
        from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
        bstack1ll111l1l1l_opy_ = bstack1llll111ll1_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack111l111111_opy_.value)
        if test != None:
            bstack11ll1llll_opy_ = getattr(test, bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᕚ"), None)
            bstack1111111l1_opy_ = getattr(test, bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᕛ"), None)
            PercySDK.screenshot(driver, bstack1l11l1l1ll_opy_, bstack11ll1llll_opy_=bstack11ll1llll_opy_, bstack1111111l1_opy_=bstack1111111l1_opy_, bstack1ll1l11l1_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l11l1l1ll_opy_)
        bstack1llll111ll1_opy_.end(EVENTS.bstack111l111111_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᕜ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᕝ"), True, None, None, None, None, test_name=bstack1l11l1l1ll_opy_)
    def bstack11llll1lll1_opy_(self):
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᕞ")] = str(self.bstack11lllll11ll_opy_.success)
        os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᕟ")] = str(self.bstack11lllll11ll_opy_.percy_capture_mode)
        self.percy.bstack11lllll11l1_opy_(self.bstack11lllll11ll_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll1111_opy_(self.bstack11lllll11ll_opy_.percy_build_id)