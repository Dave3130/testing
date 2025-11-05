# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11l1l_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1111l1_opy_ import bstack1ll11l11lll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l11lll_opy_,
    bstack1llll111111_opy_,
    bstack1lll11lll11_opy_,
    bstack1ll11l1llll_opy_,
    bstack1l1lllll1ll_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l111111_opy_
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll11111ll1_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
bstack1ll1l11lll1_opy_ = bstack1ll1l111111_opy_()
bstack1ll11ll1l1l_opy_ = bstack1lll11l_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨሒ")
bstack1ll11111l11_opy_ = bstack1lll11l_opy_ (u"ࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥሓ")
bstack1ll11l111ll_opy_ = bstack1lll11l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢሔ")
bstack1ll1l1l1l1l_opy_ = 1.0
_1ll111l1111_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll11lll111_opy_ = bstack1lll11l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤሕ")
    bstack1ll1l11ll1l_opy_ = bstack1lll11l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣሖ")
    bstack1ll1l11l111_opy_ = bstack1lll11l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥሗ")
    bstack1l1lllllll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡳࡵࡣࡵࡸࡪࡪࠢመ")
    bstack1ll111l111l_opy_ = bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤሙ")
    bstack1ll1l1l1111_opy_: bool
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_  = None
    bstack1ll11ll1lll_opy_ = [
        bstack1lll1l11lll_opy_.BEFORE_ALL,
        bstack1lll1l11lll_opy_.AFTER_ALL,
        bstack1lll1l11lll_opy_.BEFORE_EACH,
        bstack1lll1l11lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111llll1_opy_: Dict[str, str],
        bstack1l1llllll11_opy_: List[str]=[bstack1lll11l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦሚ")],
        bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_ = None,
        bstack1llll11l11l_opy_=None
    ):
        super().__init__(bstack1l1llllll11_opy_, bstack1ll111llll1_opy_, bstack1lll11l1l1l_opy_)
        self.bstack1ll1l1l1111_opy_ = any(bstack1lll11l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧማ") in item.lower() for item in bstack1l1llllll11_opy_)
        self.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
    def track_event(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l11lll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll11ll1lll_opy_:
            bstack1ll11l11lll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l11lll_opy_.NONE:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࠥሜ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠥࠦም"))
            return
        if not self.bstack1ll1l1l1111_opy_:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡁࠧሞ") + str(str(self.bstack1l1llllll11_opy_)) + bstack1lll11l_opy_ (u"ࠧࠨሟ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣሠ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠢࠣሡ"))
            return
        instance = self.__1ll11ll111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡣࡵ࡫ࡸࡃࠢሢ") + str(args) + bstack1lll11l_opy_ (u"ࠤࠥሣ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11ll1lll_opy_ and test_hook_state == bstack1lll11lll11_opy_.PRE:
                bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1ll1l1l111_opy_.value)
                name = str(EVENTS.bstack1ll1l1l111_opy_.name)+bstack1lll11l_opy_ (u"ࠥ࠾ࠧሤ")+str(test_framework_state.name)
                TestFramework.bstack1l1llllllll_opy_(instance, name, bstack1ll111111l1_opy_)
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸࠠࡱࡴࡨ࠾ࠥࢁࡽࠣሥ").format(e))
        try:
            if test_framework_state == bstack1lll1l11lll_opy_.TEST:
                if not TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_) and test_hook_state == bstack1lll11lll11_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11lll1ll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡲ࡯ࡢࡦࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧሦ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠨࠢሧ"))
                if test_hook_state == bstack1lll11lll11_opy_.PRE and not TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1l1lllll111_opy_):
                    TestFramework.bstack1llll1ll11l_opy_(instance, TestFramework.bstack1l1lllll111_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll11l11ll1_opy_(instance, args)
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡶࡸࡦࡸࡴࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧረ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠣࠤሩ"))
                elif test_hook_state == bstack1lll11lll11_opy_.POST and not TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_):
                    TestFramework.bstack1llll1ll11l_opy_(instance, TestFramework.bstack1ll111ll1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡪࡴࡤࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧሪ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠥࠦራ"))
            elif test_framework_state == bstack1lll1l11lll_opy_.STEP:
                if test_hook_state == bstack1lll11lll11_opy_.PRE:
                    PytestBDDFramework.__1l1llllll1l_opy_(instance, args)
                elif test_hook_state == bstack1lll11lll11_opy_.POST:
                    PytestBDDFramework.__1ll11l1111l_opy_(instance, args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG and test_hook_state == bstack1lll11lll11_opy_.POST:
                PytestBDDFramework.__1l1lll1ll11_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG_REPORT and test_hook_state == bstack1lll11lll11_opy_.POST:
                self.__1ll11lll11l_opy_(instance, *args)
                self.__1ll1l111lll_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll11ll1lll_opy_:
                self.__1l1lll1ll1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧሬ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠧࠨር"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll111ll111_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11ll1lll_opy_ and test_hook_state == bstack1lll11lll11_opy_.POST:
                name = str(EVENTS.bstack1ll1l1l111_opy_.name)+bstack1lll11l_opy_ (u"ࠨ࠺ࠣሮ")+str(test_framework_state.name)
                bstack1ll111111l1_opy_ = TestFramework.bstack1ll11ll1l11_opy_(instance, name)
                bstack1llll1l1l1l_opy_.end(EVENTS.bstack1ll1l1l111_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢሯ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨሰ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤሱ").format(e))
    def bstack1ll1111ll1l_opy_(self):
        return self.bstack1ll1l1l1111_opy_
    def __1ll1111l1l1_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1lll11l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢሲ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1llll1ll1_opy_(rep, [bstack1lll11l_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤሳ"), bstack1lll11l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨሴ"), bstack1lll11l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨስ"), bstack1lll11l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢሶ"), bstack1lll11l_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠤሷ"), bstack1lll11l_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣሸ")])
        return None
    def __1ll11lll11l_opy_(self, instance: bstack1llll111111_opy_, *args):
        result = self.__1ll1111l1l1_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111lll_opy_ = None
        if result.get(bstack1lll11l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦሹ"), None) == bstack1lll11l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦሺ") and len(args) > 1 and getattr(args[1], bstack1lll11l_opy_ (u"ࠧ࡫ࡸࡤ࡫ࡱࡪࡴࠨሻ"), None) is not None:
            failure = [{bstack1lll11l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩሼ"): [args[1].excinfo.exconly(), result.get(bstack1lll11l_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨሽ"), None)]}]
            bstack1111111lll_opy_ = bstack1lll11l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤሾ") if bstack1lll11l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧሿ") in getattr(args[1].excinfo, bstack1lll11l_opy_ (u"ࠥࡸࡾࡶࡥ࡯ࡣࡰࡩࠧቀ"), bstack1lll11l_opy_ (u"ࠦࠧቁ")) else bstack1lll11l_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨቂ")
        bstack1ll111l1l1l_opy_ = result.get(bstack1lll11l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢቃ"), TestFramework.bstack1ll111111ll_opy_)
        if bstack1ll111l1l1l_opy_ != TestFramework.bstack1ll111111ll_opy_:
            TestFramework.bstack1llll1ll11l_opy_(instance, TestFramework.bstack1ll1l11ll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11llll11_opy_(instance, {
            TestFramework.bstack1lll11lllll_opy_: failure,
            TestFramework.bstack1ll1111l11l_opy_: bstack1111111lll_opy_,
            TestFramework.bstack1lll1lll11l_opy_: bstack1ll111l1l1l_opy_,
        })
    def __1ll11ll111l_opy_(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l11lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l111l11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1llll1lll_opy_ bstack1ll11111lll_opy_ this to be bstack1lll11l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢቄ")
            if test_framework_state == bstack1lll1l11lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll111lllll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1lll11l_opy_ (u"ࠣࡰࡲࡨࡪࠨቅ"), None), bstack1lll11l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤቆ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1lll11l_opy_ (u"ࠥࡲࡴࡪࡥࠣቇ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1lll11l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦቈ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll1l1ll111_opy_(target) if target else None
        return instance
    def __1l1lll1ll1l_opy_(
        self,
        instance: bstack1llll111111_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1l11l1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l11ll1l_opy_, {})
        if not key in bstack1ll1l1l11l1_opy_:
            bstack1ll1l1l11l1_opy_[key] = []
        bstack1ll111l11ll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l11l111_opy_, {})
        if not key in bstack1ll111l11ll_opy_:
            bstack1ll111l11ll_opy_[key] = []
        bstack1ll1l111l1l_opy_ = {
            PytestBDDFramework.bstack1ll1l11ll1l_opy_: bstack1ll1l1l11l1_opy_,
            PytestBDDFramework.bstack1ll1l11l111_opy_: bstack1ll111l11ll_opy_,
        }
        if test_hook_state == bstack1lll11lll11_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1lll11l_opy_ (u"ࠧࡱࡥࡺࠤ቉"): key,
                TestFramework.bstack1ll1l11l1ll_opy_: uuid4().__str__(),
                TestFramework.bstack1l1llll1l1l_opy_: TestFramework.bstack1ll1l1111l1_opy_,
                TestFramework.bstack1ll11l11111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1l11l_opy_: [],
                TestFramework.bstack1l1lllll11l_opy_: hook_name,
                TestFramework.bstack1ll111lll1l_opy_: bstack1ll1l1l1ll1_opy_.bstack1ll1111ll11_opy_()
            }
            bstack1ll1l1l11l1_opy_[key].append(hook)
            bstack1ll1l111l1l_opy_[PytestBDDFramework.bstack1l1lllllll1_opy_] = key
        elif test_hook_state == bstack1lll11lll11_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1ll1l1l11l1_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1ll1111l1l1_opy_(*args)
                if result:
                    bstack1ll11l1ll1l_opy_ = result.get(bstack1lll11l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢቊ"), TestFramework.bstack1ll1l1111l1_opy_)
                    if bstack1ll11l1ll1l_opy_ != TestFramework.bstack1ll1l1111l1_opy_:
                        hook[TestFramework.bstack1l1llll1l1l_opy_] = bstack1ll11l1ll1l_opy_
                hook[TestFramework.bstack1ll11llll1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll111lll1l_opy_] = bstack1ll1l1l1ll1_opy_.bstack1ll1111ll11_opy_()
                self.bstack1l1llll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l1l1l11_opy_, [])
                self.bstack1ll1l11l1l1_opy_(instance, logs)
                bstack1ll111l11ll_opy_[key].append(hook)
                bstack1ll1l111l1l_opy_[PytestBDDFramework.bstack1ll111l111l_opy_] = key
        TestFramework.bstack1ll11llll11_opy_(instance, bstack1ll1l111l1l_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡨࡰࡱ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻ࡬ࡧࡼࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥ࠿ࡾ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࡂࠨቋ") + str(bstack1ll111l11ll_opy_) + bstack1lll11l_opy_ (u"ࠣࠤቌ"))
    def __1ll1l111l11_opy_(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1lll11lll11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1llll1ll1_opy_(args[0], [bstack1lll11l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣቍ"), bstack1lll11l_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦ቎"), bstack1lll11l_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦ቏"), bstack1lll11l_opy_ (u"ࠧ࡯ࡤࡴࠤቐ"), bstack1lll11l_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣቑ"), bstack1lll11l_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢቒ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1lll11l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢቓ")) else fixturedef.get(bstack1lll11l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣቔ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1lll11l_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣቕ")) else None
        node = request.node if hasattr(request, bstack1lll11l_opy_ (u"ࠦࡳࡵࡤࡦࠤቖ")) else None
        target = request.node.nodeid if hasattr(node, bstack1lll11l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ቗")) else None
        baseid = fixturedef.get(bstack1lll11l_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨቘ"), None) or bstack1lll11l_opy_ (u"ࠢࠣ቙")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1lll11l_opy_ (u"ࠣࡡࡳࡽ࡫ࡻ࡮ࡤ࡫ࡷࡩࡲࠨቚ")):
            target = PytestBDDFramework.__1ll11l1l111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1lll11l_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦቛ")) else None
            if target and not TestFramework.bstack1ll1l1ll111_opy_(target):
                self.__1ll111lllll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡴ࡯ࡥࡧࡀࡿࡳࡵࡤࡦࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧቜ") + str(test_hook_state) + bstack1lll11l_opy_ (u"ࠦࠧቝ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥ቞") + str(target) + bstack1lll11l_opy_ (u"ࠨࠢ቟"))
            return None
        instance = TestFramework.bstack1ll1l1ll111_opy_(target)
        if not instance:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡢࡢࡵࡨ࡭ࡩࡃࡻࡣࡣࡶࡩ࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤበ") + str(target) + bstack1lll11l_opy_ (u"ࠣࠤቡ"))
            return None
        bstack1l1llll1111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11lll111_opy_, {})
        if os.getenv(bstack1lll11l_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡈࡌ࡜࡙࡛ࡒࡆࡕࠥቢ"), bstack1lll11l_opy_ (u"ࠥ࠵ࠧባ")) == bstack1lll11l_opy_ (u"ࠦ࠶ࠨቤ"):
            bstack1ll11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡀࠢብ").join((scope, fixturename))
            bstack1ll111l1l11_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11l111l1_opy_ = {
                bstack1lll11l_opy_ (u"ࠨ࡫ࡦࡻࠥቦ"): bstack1ll11l1lll1_opy_,
                bstack1lll11l_opy_ (u"ࠢࡵࡣࡪࡷࠧቧ"): PytestBDDFramework.__1ll1111lll1_opy_(request.node, scenario),
                bstack1lll11l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࠤቨ"): fixturedef,
                bstack1lll11l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣቩ"): scope,
                bstack1lll11l_opy_ (u"ࠥࡸࡾࡶࡥࠣቪ"): None,
            }
            try:
                if test_hook_state == bstack1lll11lll11_opy_.POST and callable(getattr(args[-1], bstack1lll11l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣቫ"), None)):
                    bstack1ll11l111l1_opy_[bstack1lll11l_opy_ (u"ࠧࡺࡹࡱࡧࠥቬ")] = TestFramework.bstack1ll1111l1ll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11lll11_opy_.PRE:
                bstack1ll11l111l1_opy_[bstack1lll11l_opy_ (u"ࠨࡵࡶ࡫ࡧࠦቭ")] = uuid4().__str__()
                bstack1ll11l111l1_opy_[PytestBDDFramework.bstack1ll11l11111_opy_] = bstack1ll111l1l11_opy_
            elif test_hook_state == bstack1lll11lll11_opy_.POST:
                bstack1ll11l111l1_opy_[PytestBDDFramework.bstack1ll11llll1l_opy_] = bstack1ll111l1l11_opy_
            if bstack1ll11l1lll1_opy_ in bstack1l1llll1111_opy_:
                bstack1l1llll1111_opy_[bstack1ll11l1lll1_opy_].update(bstack1ll11l111l1_opy_)
                self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࠣቮ") + str(bstack1l1llll1111_opy_[bstack1ll11l1lll1_opy_]) + bstack1lll11l_opy_ (u"ࠣࠤቯ"))
            else:
                bstack1l1llll1111_opy_[bstack1ll11l1lll1_opy_] = bstack1ll11l111l1_opy_
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡽࠡࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࠧተ") + str(len(bstack1l1llll1111_opy_)) + bstack1lll11l_opy_ (u"ࠥࠦቱ"))
        TestFramework.bstack1llll1ll11l_opy_(instance, PytestBDDFramework.bstack1ll11lll111_opy_, bstack1l1llll1111_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࢁ࡬ࡦࡰࠫࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸ࠯ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦቲ") + str(instance.ref()) + bstack1lll11l_opy_ (u"ࠧࠨታ"))
        return instance
    def __1ll111lllll_opy_(
        self,
        context: bstack1ll11l1llll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        ob = bstack1llll111111_opy_(ctx, self.bstack1l1llllll11_opy_, self.bstack1ll111llll1_opy_, test_framework_state)
        TestFramework.bstack1ll11llll11_opy_(ob, {
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1l111_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1ll11_opy_: [],
            PytestBDDFramework.bstack1ll11lll111_opy_: {},
            PytestBDDFramework.bstack1ll1l11l111_opy_: {},
            PytestBDDFramework.bstack1ll1l11ll1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1ll11l_opy_(ob, TestFramework.bstack1ll111ll1l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1ll11l_opy_(ob, TestFramework.bstack1lllllllll1_opy_, context.platform_index)
        TestFramework.bstack1llll111ll1_opy_[ctx.id] = ob
        self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡤࡶࡻ࠲࡮ࡪ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨቴ") + str(TestFramework.bstack1llll111ll1_opy_.keys()) + bstack1lll11l_opy_ (u"ࠢࠣት"))
        return ob
    @staticmethod
    def __1ll11l11ll1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lll11l_opy_ (u"ࠨ࡫ࡧࠫቶ"): id(step),
                bstack1lll11l_opy_ (u"ࠩࡷࡩࡽࡺࠧቷ"): step.name,
                bstack1lll11l_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫቸ"): step.keyword,
            })
        meta = {
            bstack1lll11l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬቹ"): {
                bstack1lll11l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪቺ"): feature.name,
                bstack1lll11l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫቻ"): feature.filename,
                bstack1lll11l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬቼ"): feature.description
            },
            bstack1lll11l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪች"): {
                bstack1lll11l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧቾ"): scenario.name
            },
            bstack1lll11l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩቿ"): steps,
            bstack1lll11l_opy_ (u"ࠫࡪࡾࡡ࡮ࡲ࡯ࡩࡸ࠭ኀ"): PytestBDDFramework.__1ll11lll1l1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll1111l111_opy_: meta
            }
        )
    def bstack1l1llll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኁ")
        global _1ll111l1111_opy_
        platform_index = os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ኂ")]
        bstack1ll11lllll1_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1ll11ll1l1l_opy_ + str(platform_index)), bstack1ll11111l11_opy_)
        if not os.path.exists(bstack1ll11lllll1_opy_) or not os.path.isdir(bstack1ll11lllll1_opy_):
            return
        logs = hook.get(bstack1lll11l_opy_ (u"ࠢ࡭ࡱࡪࡷࠧኃ"), [])
        with os.scandir(bstack1ll11lllll1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll111l1111_opy_:
                    self.logger.info(bstack1lll11l_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨኄ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1lll11l_opy_ (u"ࠤࠥኅ")
                    log_entry = bstack1l1lllll1ll_opy_(
                        kind=bstack1lll11l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧኆ"),
                        message=bstack1lll11l_opy_ (u"ࠦࠧኇ"),
                        level=bstack1lll11l_opy_ (u"ࠧࠨኈ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11111l1l_opy_=entry.stat().st_size,
                        bstack1ll1l1l111l_opy_=bstack1lll11l_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨ኉"),
                        bstack1ll111l_opy_=os.path.abspath(entry.path),
                        bstack1ll1l11111l_opy_=hook.get(TestFramework.bstack1ll1l11l1ll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll111l1111_opy_.add(abs_path)
        platform_index = os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧኊ")]
        bstack1ll111l1lll_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1ll11ll1l1l_opy_ + str(platform_index)), bstack1ll11111l11_opy_, bstack1ll11l111ll_opy_)
        if not os.path.exists(bstack1ll111l1lll_opy_) or not os.path.isdir(bstack1ll111l1lll_opy_):
            self.logger.info(bstack1lll11l_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥኋ").format(bstack1ll111l1lll_opy_))
        else:
            self.logger.info(bstack1lll11l_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣኌ").format(bstack1ll111l1lll_opy_))
            with os.scandir(bstack1ll111l1lll_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll111l1111_opy_:
                        self.logger.info(bstack1lll11l_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣኍ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1lll11l_opy_ (u"ࠦࠧ኎")
                        log_entry = bstack1l1lllll1ll_opy_(
                            kind=bstack1lll11l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢ኏"),
                            message=bstack1lll11l_opy_ (u"ࠨࠢነ"),
                            level=bstack1lll11l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦኑ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11111l1l_opy_=entry.stat().st_size,
                            bstack1ll1l1l111l_opy_=bstack1lll11l_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣኒ"),
                            bstack1ll111l_opy_=os.path.abspath(entry.path),
                            bstack1ll1l1l1lll_opy_=hook.get(TestFramework.bstack1ll1l11l1ll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll111l1111_opy_.add(abs_path)
        hook[bstack1lll11l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢና")] = logs
    def bstack1ll1l11l1l1_opy_(
        self,
        bstack1ll1l11llll_opy_: bstack1llll111111_opy_,
        entries: List[bstack1l1lllll1ll_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1lll11l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢኔ"))
        req.platform_index = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lllllllll1_opy_)
        req.execution_context.hash = str(bstack1ll1l11llll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1l11llll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1l11llll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lll1l1l111_opy_)
            log_entry.uuid = entry.bstack1ll1l11111l_opy_ if entry.bstack1ll1l11111l_opy_ else TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lll11ll11l_opy_)
            log_entry.test_framework_state = bstack1ll1l11llll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lll11l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥን"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1lll11l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢኖ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11111l1l_opy_
                log_entry.file_path = entry.bstack1ll111l_opy_
        def bstack1l1llll1l11_opy_():
            bstack11ll11l1l_opy_ = datetime.now()
            try:
                self.bstack1llll11l11l_opy_.LogCreatedEvent(req)
                bstack1ll1l11llll_opy_.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥኗ"), datetime.now() - bstack11ll11l1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lll11l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡿࢂࠨኘ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1l1llll1l11_opy_)
    def __1ll1l111lll_opy_(self, instance) -> None:
        bstack1lll11l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡒ࡯ࡢࡦࡶࠤࡨࡻࡳࡵࡱࡰࠤࡹࡧࡧࡴࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡨ࡮ࡩࡴࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡧࡴࡲࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡶࡵࡷࡳࡲ࡚ࡡࡨࡏࡤࡲࡦ࡭ࡥࡳࠢࡤࡲࡩࠦࡵࡱࡦࡤࡸࡪࡹࠠࡵࡪࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡳࡵࡣࡷࡩࠥࡻࡳࡪࡰࡪࠤࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࡟ࡦࡰࡷࡶ࡮࡫ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨኙ")
        bstack1ll1l111l1l_opy_ = {bstack1lll11l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡡࡰࡩࡹࡧࡤࡢࡶࡤࠦኚ"): bstack1ll1l1l1ll1_opy_.bstack1ll1111ll11_opy_()}
        TestFramework.bstack1ll11llll11_opy_(instance, bstack1ll1l111l1l_opy_)
    @staticmethod
    def __1l1llllll1l_opy_(instance, args):
        request, bstack1l1lll1llll_opy_ = args
        bstack1ll1l111ll1_opy_ = id(bstack1l1lll1llll_opy_)
        bstack1ll1111111l_opy_ = instance.data[TestFramework.bstack1ll1111l111_opy_]
        step = next(filter(lambda st: st[bstack1lll11l_opy_ (u"ࠪ࡭ࡩ࠭ኛ")] == bstack1ll1l111ll1_opy_, bstack1ll1111111l_opy_[bstack1lll11l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኜ")]), None)
        step.update({
            bstack1lll11l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩኝ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll1111111l_opy_[bstack1lll11l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኞ")]) if st[bstack1lll11l_opy_ (u"ࠧࡪࡦࠪኟ")] == step[bstack1lll11l_opy_ (u"ࠨ࡫ࡧࠫአ")]), None)
        if index is not None:
            bstack1ll1111111l_opy_[bstack1lll11l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኡ")][index] = step
        instance.data[TestFramework.bstack1ll1111l111_opy_] = bstack1ll1111111l_opy_
    @staticmethod
    def __1ll11l1111l_opy_(instance, args):
        bstack1lll11l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡸࡪࡨࡲࠥࡲࡥ࡯ࠢࡤࡶ࡬ࡹࠠࡪࡵࠣ࠶࠱ࠦࡩࡵࠢࡶ࡭࡬ࡴࡩࡧ࡫ࡨࡷࠥࡺࡨࡦࡴࡨࠤ࡮ࡹࠠ࡯ࡱࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠭ࠡ࡝ࡵࡩࡶࡻࡥࡴࡶ࠯ࠤࡸࡺࡥࡱ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠶ࠤࡹ࡮ࡥ࡯ࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡻࡧ࡬ࡶࡧࠣ࡭ࡸࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨኢ")
        bstack1ll111lll11_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l1lll1llll_opy_ = args[1]
        bstack1ll1l111ll1_opy_ = id(bstack1l1lll1llll_opy_)
        bstack1ll1111111l_opy_ = instance.data[TestFramework.bstack1ll1111l111_opy_]
        step = None
        if bstack1ll1l111ll1_opy_ is not None and bstack1ll1111111l_opy_.get(bstack1lll11l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኣ")):
            step = next(filter(lambda st: st[bstack1lll11l_opy_ (u"ࠬ࡯ࡤࠨኤ")] == bstack1ll1l111ll1_opy_, bstack1ll1111111l_opy_[bstack1lll11l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬእ")]), None)
            step.update({
                bstack1lll11l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬኦ"): bstack1ll111lll11_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1lll11l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨኧ"): bstack1lll11l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩከ"),
                bstack1lll11l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫኩ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫኪ"): bstack1lll11l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬካ"),
                })
        index = next((i for i, st in enumerate(bstack1ll1111111l_opy_[bstack1lll11l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኬ")]) if st[bstack1lll11l_opy_ (u"ࠧࡪࡦࠪክ")] == step[bstack1lll11l_opy_ (u"ࠨ࡫ࡧࠫኮ")]), None)
        if index is not None:
            bstack1ll1111111l_opy_[bstack1lll11l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኯ")][index] = step
        instance.data[TestFramework.bstack1ll1111l111_opy_] = bstack1ll1111111l_opy_
    @staticmethod
    def __1ll11lll1l1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1lll11l_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬኰ")):
                examples = list(node.callspec.params[bstack1lll11l_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪ኱")].values())
            return examples
        except:
            return []
    def bstack1ll1l11l11l_opy_(self, instance: bstack1llll111111_opy_, bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_]):
        bstack1ll111ll11l_opy_ = (
            PytestBDDFramework.bstack1l1lllllll1_opy_
            if bstack1lllll1l111_opy_[1] == bstack1lll11lll11_opy_.PRE
            else PytestBDDFramework.bstack1ll111l111l_opy_
        )
        hook = PytestBDDFramework.bstack1ll11ll11ll_opy_(instance, bstack1ll111ll11l_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1l11l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll11_opy_, []))
        return entries
    def bstack1ll11l11l11_opy_(self, instance: bstack1llll111111_opy_, bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_]):
        bstack1ll111ll11l_opy_ = (
            PytestBDDFramework.bstack1l1lllllll1_opy_
            if bstack1lllll1l111_opy_[1] == bstack1lll11lll11_opy_.PRE
            else PytestBDDFramework.bstack1ll111l111l_opy_
        )
        PytestBDDFramework.bstack1ll11ll1111_opy_(instance, bstack1ll111ll11l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll11_opy_, []).clear()
    @staticmethod
    def bstack1ll11ll11ll_opy_(instance: bstack1llll111111_opy_, bstack1ll111ll11l_opy_: str):
        bstack1ll1111llll_opy_ = (
            PytestBDDFramework.bstack1ll1l11l111_opy_
            if bstack1ll111ll11l_opy_ == PytestBDDFramework.bstack1ll111l111l_opy_
            else PytestBDDFramework.bstack1ll1l11ll1l_opy_
        )
        bstack1l1llll11l1_opy_ = TestFramework.get_state(instance, bstack1ll111ll11l_opy_, None)
        bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1ll1111llll_opy_, None) if bstack1l1llll11l1_opy_ else None
        return (
            bstack1ll11llllll_opy_[bstack1l1llll11l1_opy_][-1]
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1l1llll11l1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11ll1111_opy_(instance: bstack1llll111111_opy_, bstack1ll111ll11l_opy_: str):
        hook = PytestBDDFramework.bstack1ll11ll11ll_opy_(instance, bstack1ll111ll11l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1l11l_opy_, []).clear()
    @staticmethod
    def __1l1lll1ll11_opy_(instance: bstack1llll111111_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1lll11l_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥኲ"), None)):
            return
        if os.getenv(bstack1lll11l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥኳ"), bstack1lll11l_opy_ (u"ࠢ࠲ࠤኴ")) != bstack1lll11l_opy_ (u"ࠣ࠳ࠥኵ"):
            PytestBDDFramework.logger.warning(bstack1lll11l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦ኶"))
            return
        bstack1l1llll11ll_opy_ = {
            bstack1lll11l_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ኷"): (PytestBDDFramework.bstack1l1lllllll1_opy_, PytestBDDFramework.bstack1ll1l11ll1l_opy_),
            bstack1lll11l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨኸ"): (PytestBDDFramework.bstack1ll111l111l_opy_, PytestBDDFramework.bstack1ll1l11l111_opy_),
        }
        for when in (bstack1lll11l_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦኹ"), bstack1lll11l_opy_ (u"ࠨࡣࡢ࡮࡯ࠦኺ"), bstack1lll11l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤኻ")):
            bstack1ll11111111_opy_ = args[1].get_records(when)
            if not bstack1ll11111111_opy_:
                continue
            records = [
                bstack1l1lllll1ll_opy_(
                    kind=TestFramework.bstack1l1lllll1l1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1lll11l_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦኼ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1lll11l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥኽ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11111111_opy_
                if isinstance(getattr(r, bstack1lll11l_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦኾ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l11l1l_opy_, bstack1ll1111llll_opy_ = bstack1l1llll11ll_opy_.get(when, (None, None))
            bstack1ll11l1l1ll_opy_ = TestFramework.get_state(instance, bstack1ll11l11l1l_opy_, None) if bstack1ll11l11l1l_opy_ else None
            bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1ll1111llll_opy_, None) if bstack1ll11l1l1ll_opy_ else None
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1ll11l1l1ll_opy_, [])) > 0:
                hook = bstack1ll11llllll_opy_[bstack1ll11l1l1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1l11l_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1l11l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll11_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11lll1ll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1l1111ll_opy_(request.node, scenario)
        bstack1ll1l1ll11l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll1l1ll11l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll11ll11l_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11l1l1l1_opy_: test_id,
            TestFramework.bstack1l1lll1l1ll_opy_: test_name,
            TestFramework.bstack1ll1l1l11ll_opy_: test_id,
            TestFramework.bstack1ll11ll1ll1_opy_: bstack1ll1l1ll11l_opy_,
            TestFramework.bstack1l1lll1lll1_opy_: PytestBDDFramework.__1ll1111lll1_opy_(feature, scenario),
            TestFramework.bstack1ll11ll11l1_opy_: code,
            TestFramework.bstack1lll1lll11l_opy_: TestFramework.bstack1ll111111ll_opy_,
            TestFramework.bstack1lll1111lll_opy_: test_name
        }
    @staticmethod
    def __1ll1l1111ll_opy_(node, scenario):
        if hasattr(node, bstack1lll11l_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭኿")):
            parts = node.nodeid.rsplit(bstack1lll11l_opy_ (u"ࠧࡡࠢዀ"))
            params = parts[-1]
            return bstack1lll11l_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨ዁").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll1111lll1_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1lll11l_opy_ (u"ࠧࡵࡣࡪࡷࠬዂ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1lll11l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ዃ")) else [])
    @staticmethod
    def __1ll11l1l111_opy_(location):
        return bstack1lll11l_opy_ (u"ࠤ࠽࠾ࠧዄ").join(filter(lambda x: isinstance(x, str), location))