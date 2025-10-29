# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import (
    bstack1lllll1l1ll_opy_,
    bstack1llllll11ll_opy_,
    bstack1llll1llll1_opy_,
)
from bstack_utils.helper import  bstack1l11l111_opy_
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11l1_opy_, bstack1lll1l1l11l_opy_, bstack1lll1l1llll_opy_, bstack1ll1l1l1l11_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack111l111ll1_opy_ import bstack111111l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111l1l_opy_ import bstack1lll111l1l1_opy_
from bstack_utils.percy import bstack11lll11111_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11llll111_opy_(bstack1lllll11111_opy_):
    def __init__(self, bstack11llll1l1ll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llll1l1ll_opy_ = bstack11llll1l1ll_opy_
        self.percy = bstack11lll11111_opy_()
        self.bstack1l1111lll_opy_ = bstack111111l1l_opy_()
        self.bstack11llll1ll11_opy_()
        bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, bstack1llllll11ll_opy_.PRE), self.bstack11llll1lll1_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.POST), self.bstack1lll1ll1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l111lllll1_opy_(self, instance: bstack1llll1llll1_opy_, driver: object):
        bstack1l11l1111ll_opy_ = TestFramework.bstack1l11l1l1111_opy_(instance.context)
        for t in bstack1l11l1111ll_opy_:
            bstack1lll111ll11_opy_ = TestFramework.get_state(t, bstack1lll111l1l1_opy_.bstack1lll1ll1l1l_opy_, [])
            if any(instance is d[1] for d in bstack1lll111ll11_opy_) or instance == driver:
                return t
    def bstack11llll1lll1_opy_(
        self,
        f: bstack1llll1l111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll1l111l_opy_.bstack1l1ll1ll1ll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll1lll11_opy_, 0)
            bstack1ll1111ll11_opy_ = self.bstack1l111lllll1_opy_(instance, driver)
            bstack11lllll11l1_opy_ = TestFramework.get_state(bstack1ll1111ll11_opy_, TestFramework.bstack1ll1l11111l_opy_, None)
            if not bstack11lllll11l1_opy_:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡸࡥࡵࡷࡵࡲ࡮ࡴࡧࠡࡣࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡯ࡳࠡࡰࡲࡸࠥࡿࡥࡵࠢࡶࡸࡦࡸࡴࡦࡦࠥᕉ"))
                return
            driver_command = f.bstack1l1ll1l1lll_opy_(*args)
            for command in bstack111ll1l11_opy_:
                if command == driver_command:
                    self.bstack1llll1l1l1_opy_(driver, platform_index)
            bstack11l1lll1l_opy_ = self.percy.bstack1ll11llll_opy_()
            if driver_command in bstack1l1lll1ll_opy_[bstack11l1lll1l_opy_]:
                self.bstack1l1111lll_opy_.bstack11ll1l1l11_opy_(bstack11lllll11l1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠦࡴࡴ࡟ࡱࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡥࡳࡴࡲࡶࠧᕊ"), e)
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l11l_opy_,
        bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1l111l1l1_opy_ import bstack1lllllll1ll_opy_
        bstack1lll111ll11_opy_ = f.get_state(instance, bstack1lll111l1l1_opy_.bstack1lll1ll1l1l_opy_, [])
        if not bstack1lll111ll11_opy_:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕋ") + str(kwargs) + bstack11l11ll_opy_ (u"ࠨࠢᕌ"))
            return
        if len(bstack1lll111ll11_opy_) > 1:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᕍ") + str(kwargs) + bstack11l11ll_opy_ (u"ࠣࠤᕎ"))
        bstack1lll11111l1_opy_, bstack1llll111111_opy_ = bstack1lll111ll11_opy_[0]
        driver = bstack1lll11111l1_opy_()
        if not driver:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕏ") + str(kwargs) + bstack11l11ll_opy_ (u"ࠥࠦᕐ"))
            return
        bstack11llll1l1l1_opy_ = {
            TestFramework.bstack1l1lll1llll_opy_: bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᕑ"),
            TestFramework.bstack1lll11l1lll_opy_: bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᕒ"),
            TestFramework.bstack1ll1l11111l_opy_: bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࠤࡷ࡫ࡲࡶࡰࠣࡲࡦࡳࡥࠣᕓ")
        }
        bstack11lllll1111_opy_ = { key: f.get_state(instance, key) for key in bstack11llll1l1l1_opy_ }
        bstack11lllll11ll_opy_ = [key for key, value in bstack11lllll1111_opy_.items() if not value]
        if bstack11lllll11ll_opy_:
            for key in bstack11lllll11ll_opy_:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠥᕔ") + str(key) + bstack11l11ll_opy_ (u"ࠣࠤᕕ"))
            return
        platform_index = f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll1lll11_opy_, 0)
        if self.bstack11llll1l1ll_opy_.percy_capture_mode == bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᕖ"):
            bstack11ll11l1l1_opy_ = bstack11lllll1111_opy_.get(TestFramework.bstack1ll1l11111l_opy_) + bstack11l11ll_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᕗ")
            bstack1ll11l11lll_opy_ = bstack1lllllll1ll_opy_.bstack1ll11l111ll_opy_(EVENTS.bstack11llll1ll1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11ll11l1l1_opy_,
                bstack1ll11llll1_opy_=bstack11lllll1111_opy_[TestFramework.bstack1l1lll1llll_opy_],
                bstack1l1lll111l_opy_=bstack11lllll1111_opy_[TestFramework.bstack1lll11l1lll_opy_],
                bstack11111l11ll_opy_=platform_index
            )
            bstack1lllllll1ll_opy_.end(EVENTS.bstack11llll1ll1l_opy_.value, bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕘ"), bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕙ"), True, None, None, None, None, test_name=bstack11ll11l1l1_opy_)
    def bstack1llll1l1l1_opy_(self, driver, platform_index):
        if self.bstack1l1111lll_opy_.bstack1ll1l11111_opy_() is True or self.bstack1l1111lll_opy_.capturing() is True:
            return
        self.bstack1l1111lll_opy_.bstack1lll11l111_opy_()
        while not self.bstack1l1111lll_opy_.bstack1ll1l11111_opy_():
            bstack11lllll11l1_opy_ = self.bstack1l1111lll_opy_.bstack1lll111111_opy_()
            self.bstack11ll1l1lll_opy_(driver, bstack11lllll11l1_opy_, platform_index)
        self.bstack1l1111lll_opy_.bstack11lllll111_opy_()
    def bstack11ll1l1lll_opy_(self, driver, bstack111ll1111l_opy_, platform_index, test=None):
        from bstack_utils.bstack1l111l1l1_opy_ import bstack1lllllll1ll_opy_
        bstack1ll11l11lll_opy_ = bstack1lllllll1ll_opy_.bstack1ll11l111ll_opy_(EVENTS.bstack111l1l1lll_opy_.value)
        if test != None:
            bstack1ll11llll1_opy_ = getattr(test, bstack11l11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᕚ"), None)
            bstack1l1lll111l_opy_ = getattr(test, bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᕛ"), None)
            PercySDK.screenshot(driver, bstack111ll1111l_opy_, bstack1ll11llll1_opy_=bstack1ll11llll1_opy_, bstack1l1lll111l_opy_=bstack1l1lll111l_opy_, bstack11111l11ll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack111ll1111l_opy_)
        bstack1lllllll1ll_opy_.end(EVENTS.bstack111l1l1lll_opy_.value, bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᕜ"), bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᕝ"), True, None, None, None, None, test_name=bstack111ll1111l_opy_)
    def bstack11llll1ll11_opy_(self):
        os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᕞ")] = str(self.bstack11llll1l1ll_opy_.success)
        os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᕟ")] = str(self.bstack11llll1l1ll_opy_.percy_capture_mode)
        self.percy.bstack11lllll111l_opy_(self.bstack11llll1l1ll_opy_.is_percy_auto_enabled)
        self.percy.bstack11llll1llll_opy_(self.bstack11llll1l1ll_opy_.percy_build_id)