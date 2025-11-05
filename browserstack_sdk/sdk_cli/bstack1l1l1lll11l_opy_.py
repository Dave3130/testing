# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll11l1_opy_ import bstack1ll1ll11111_opy_
from browserstack_sdk.sdk_cli.utils.bstack11ll1111l_opy_ import bstack1ll11l1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l111l1_opy_,
    bstack1lll1l1l1ll_opy_,
    bstack1lll1ll1ll1_opy_,
    bstack1ll1l111lll_opy_,
    bstack1l1llll111l_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l1l11l1_opy_
from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll111llll_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11l11l1l_opy_ import bstack1ll11llll11_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1l11l1l1_opy_
bstack1ll111l1l1l_opy_ = bstack1ll1l1l11l1_opy_()
bstack1l1lll1ll11_opy_ = 1.0
bstack1l1lll1l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᖩ")
bstack11lll1ll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᖪ")
bstack11lll1ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᖫ")
bstack11lll1l1lll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢᖬ")
bstack11lll1ll111_opy_ = bstack11ll1ll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦᖭ")
_1ll1l1l1l11_opy_ = set()
class bstack1l11lll1lll_opy_(TestFramework):
    bstack1ll111lll1l_opy_ = bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᖮ")
    bstack1ll11l1111l_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࠧᖯ")
    bstack1ll111llll1_opy_ = bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᖰ")
    bstack1l1lllll11l_opy_ = bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࠦᖱ")
    bstack1l1llllll11_opy_ = bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᖲ")
    bstack1l1lll1ll1l_opy_: bool
    bstack1lll111llll_opy_: bstack1lll11l111l_opy_  = None
    bstack1llllll1l1l_opy_ = None
    bstack1ll1l1l1l1l_opy_ = [
        bstack1lll1l111l1_opy_.BEFORE_ALL,
        bstack1lll1l111l1_opy_.AFTER_ALL,
        bstack1lll1l111l1_opy_.BEFORE_EACH,
        bstack1lll1l111l1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11ll1l11_opy_: Dict[str, str],
        bstack1ll1l11111l_opy_: List[str]=[bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᖳ")],
        bstack1lll111llll_opy_: bstack1lll11l111l_opy_=None,
        bstack1llllll1l1l_opy_=None
    ):
        super().__init__(bstack1ll1l11111l_opy_, bstack1ll11ll1l11_opy_, bstack1lll111llll_opy_)
        self.bstack1l1lll1ll1l_opy_ = any(bstack11ll1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᖴ") in item.lower() for item in bstack1ll1l11111l_opy_)
        self.bstack1llllll1l1l_opy_ = bstack1llllll1l1l_opy_
    def track_event(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l111l1_opy_.TEST or test_framework_state in bstack1l11lll1lll_opy_.bstack1ll1l1l1l1l_opy_:
            bstack1ll11l1l1l1_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l111l1_opy_.NONE:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࠢᖵ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠢࠣᖶ"))
            return
        if not self.bstack1l1lll1ll1l_opy_:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠾ࠤᖷ") + str(str(self.bstack1ll1l11111l_opy_)) + bstack11ll1ll_opy_ (u"ࠤࠥᖸ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᖹ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠦࠧᖺ"))
            return
        instance = self.__1ll111l1lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡧࡲࡨࡵࡀࠦᖻ") + str(args) + bstack11ll1ll_opy_ (u"ࠨࠢᖼ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11lll1lll_opy_.bstack1ll1l1l1l1l_opy_ and test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack11lll1l1ll_opy_.value)
                name = str(EVENTS.bstack11lll1l1ll_opy_.name)+bstack11ll1ll_opy_ (u"ࠢ࠻ࠤᖽ")+str(test_framework_state.name)
                TestFramework.bstack1ll11ll11ll_opy_(instance, name, bstack1l1lll1l1ll_opy_)
        except Exception as e:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵࠤࡵࡸࡥ࠻ࠢࡾࢁࠧᖾ").format(e))
        try:
            if not TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1ll1l11llll_opy_) and test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                test = bstack1l11lll1lll_opy_.__1ll1111ll1l_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠤ࡯ࡳࡦࡪࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᖿ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠥࠦᗀ"))
            if test_framework_state == bstack1lll1l111l1_opy_.TEST:
                if test_hook_state == bstack1lll1ll1ll1_opy_.PRE and not TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1ll1l11ll1l_opy_):
                    TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l11ll1l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡳࡵࡣࡵࡸࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᗁ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠧࠨᗂ"))
                elif test_hook_state == bstack1lll1ll1ll1_opy_.POST and not TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_):
                    TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡧࡱࡨࠥ࡬࡯ࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᗃ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠢࠣᗄ"))
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG and test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                bstack1l11lll1lll_opy_.__1ll111111ll_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG_REPORT and test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                self.__1ll1l11l1ll_opy_(instance, *args)
                self.__1ll111111l1_opy_(instance)
            elif test_framework_state in bstack1l11lll1lll_opy_.bstack1ll1l1l1l1l_opy_:
                self.__1ll111ll111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᗅ") + str(instance.ref()) + bstack11ll1ll_opy_ (u"ࠤࠥᗆ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11l1lll1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11lll1lll_opy_.bstack1ll1l1l1l1l_opy_ and test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                name = str(EVENTS.bstack11lll1l1ll_opy_.name)+bstack11ll1ll_opy_ (u"ࠥ࠾ࠧᗇ")+str(test_framework_state.name)
                bstack1l1lll1l1ll_opy_ = TestFramework.bstack1ll11lllll1_opy_(instance, name)
                bstack1llll11l11l_opy_.end(EVENTS.bstack11lll1l1ll_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᗈ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᗉ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᗊ").format(e))
    def bstack1l1lllll111_opy_(self):
        return self.bstack1l1lll1ll1l_opy_
    def __1ll11111l11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11ll1ll_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᗋ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1llll1lll_opy_(rep, [bstack11ll1ll_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᗌ"), bstack11ll1ll_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᗍ"), bstack11ll1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᗎ"), bstack11ll1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᗏ"), bstack11ll1ll_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨᗐ"), bstack11ll1ll_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᗑ")])
        return None
    def __1ll1l11l1ll_opy_(self, instance: bstack1lll1l1l1ll_opy_, *args):
        result = self.__1ll11111l11_opy_(*args)
        if not result:
            return
        failure = None
        bstack1111111l11_opy_ = None
        if result.get(bstack11ll1ll_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᗒ"), None) == bstack11ll1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᗓ") and len(args) > 1 and getattr(args[1], bstack11ll1ll_opy_ (u"ࠤࡨࡼࡨ࡯࡮ࡧࡱࠥᗔ"), None) is not None:
            failure = [{bstack11ll1ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᗕ"): [args[1].excinfo.exconly(), result.get(bstack11ll1ll_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥᗖ"), None)]}]
            bstack1111111l11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᗗ") if bstack11ll1ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᗘ") in getattr(args[1].excinfo, bstack11ll1ll_opy_ (u"ࠢࡵࡻࡳࡩࡳࡧ࡭ࡦࠤᗙ"), bstack11ll1ll_opy_ (u"ࠣࠤᗚ")) else bstack11ll1ll_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᗛ")
        bstack1l1lll1l11l_opy_ = result.get(bstack11ll1ll_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᗜ"), TestFramework.bstack1l1lll1lll1_opy_)
        if bstack1l1lll1l11l_opy_ != TestFramework.bstack1l1lll1lll1_opy_:
            TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1l1lll1llll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11ll1l1l_opy_(instance, {
            TestFramework.bstack1lll1l1111l_opy_: failure,
            TestFramework.bstack1ll1l11l1l1_opy_: bstack1111111l11_opy_,
            TestFramework.bstack1llll1111l1_opy_: bstack1l1lll1l11l_opy_,
        })
    def __1ll111l1lll_opy_(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l111l1_opy_.SETUP_FIXTURE:
            instance = self.__1ll11l1l11l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1111lll1_opy_ bstack1ll1l1111l1_opy_ this to be bstack11ll1ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᗝ")
            if test_framework_state == bstack1lll1l111l1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1llllllll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᗞ"), None), bstack11ll1ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᗟ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11ll1ll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᗠ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11l1ll11_opy_(target) if target else None
        return instance
    def __1ll111ll111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll111l1ll1_opy_ = TestFramework.get_state(instance, bstack1l11lll1lll_opy_.bstack1ll11l1111l_opy_, {})
        if not key in bstack1ll111l1ll1_opy_:
            bstack1ll111l1ll1_opy_[key] = []
        bstack1ll11l11ll1_opy_ = TestFramework.get_state(instance, bstack1l11lll1lll_opy_.bstack1ll111llll1_opy_, {})
        if not key in bstack1ll11l11ll1_opy_:
            bstack1ll11l11ll1_opy_[key] = []
        bstack1ll1l1l1111_opy_ = {
            bstack1l11lll1lll_opy_.bstack1ll11l1111l_opy_: bstack1ll111l1ll1_opy_,
            bstack1l11lll1lll_opy_.bstack1ll111llll1_opy_: bstack1ll11l11ll1_opy_,
        }
        if test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
            hook = {
                bstack11ll1ll_opy_ (u"ࠣ࡭ࡨࡽࠧᗡ"): key,
                TestFramework.bstack1ll1l11l11l_opy_: uuid4().__str__(),
                TestFramework.bstack1l1llll1l1l_opy_: TestFramework.bstack1ll1111l11l_opy_,
                TestFramework.bstack1l1lllll1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1l111_opy_: [],
                TestFramework.bstack1ll11111111_opy_: args[1] if len(args) > 1 else bstack11ll1ll_opy_ (u"ࠩࠪᗢ"),
                TestFramework.bstack1ll1l111l1l_opy_: bstack1ll11llll11_opy_.bstack1ll11llll1l_opy_()
            }
            bstack1ll111l1ll1_opy_[key].append(hook)
            bstack1ll1l1l1111_opy_[bstack1l11lll1lll_opy_.bstack1l1lllll11l_opy_] = key
        elif test_hook_state == bstack1lll1ll1ll1_opy_.POST:
            bstack1l1llll1ll1_opy_ = bstack1ll111l1ll1_opy_.get(key, [])
            hook = bstack1l1llll1ll1_opy_.pop() if bstack1l1llll1ll1_opy_ else None
            if hook:
                result = self.__1ll11111l11_opy_(*args)
                if result:
                    bstack1ll11lll111_opy_ = result.get(bstack11ll1ll_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦᗣ"), TestFramework.bstack1ll1111l11l_opy_)
                    if bstack1ll11lll111_opy_ != TestFramework.bstack1ll1111l11l_opy_:
                        hook[TestFramework.bstack1l1llll1l1l_opy_] = bstack1ll11lll111_opy_
                hook[TestFramework.bstack1ll1l111ll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l111l1l_opy_]= bstack1ll11llll11_opy_.bstack1ll11llll1l_opy_()
                self.bstack1ll11111ll1_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1111ll11_opy_, [])
                if logs: self.bstack1ll1111l111_opy_(instance, logs)
                bstack1ll11l11ll1_opy_[key].append(hook)
                bstack1ll1l1l1111_opy_[bstack1l11lll1lll_opy_.bstack1l1llllll11_opy_] = key
        TestFramework.bstack1ll11ll1l1l_opy_(instance, bstack1ll1l1l1111_opy_)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢ࡬ࡴࡵ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡰ࡫ࡹࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࡃࡻࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࡽࠡࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥ࠿ࠥᗤ") + str(bstack1ll11l11ll1_opy_) + bstack11ll1ll_opy_ (u"ࠧࠨᗥ"))
    def __1ll11l1l11l_opy_(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1llll1lll_opy_(args[0], [bstack11ll1ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗦ"), bstack11ll1ll_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᗧ"), bstack11ll1ll_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᗨ"), bstack11ll1ll_opy_ (u"ࠤ࡬ࡨࡸࠨᗩ"), bstack11ll1ll_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᗪ"), bstack11ll1ll_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦᗫ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11ll1ll_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗬ")) else fixturedef.get(bstack11ll1ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᗭ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11ll1ll_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࠧᗮ")) else None
        node = request.node if hasattr(request, bstack11ll1ll_opy_ (u"ࠣࡰࡲࡨࡪࠨᗯ")) else None
        target = request.node.nodeid if hasattr(node, bstack11ll1ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᗰ")) else None
        baseid = fixturedef.get(bstack11ll1ll_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᗱ"), None) or bstack11ll1ll_opy_ (u"ࠦࠧᗲ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11ll1ll_opy_ (u"ࠧࡥࡰࡺࡨࡸࡲࡨ࡯ࡴࡦ࡯ࠥᗳ")):
            target = bstack1l11lll1lll_opy_.__1ll11ll111l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11ll1ll_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᗴ")) else None
            if target and not TestFramework.bstack1ll11l1ll11_opy_(target):
                self.__1l1llllllll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡱࡳࡩ࡫࠽ࡼࡰࡲࡨࡪࢃࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࠤᗵ") + str(test_hook_state) + bstack11ll1ll_opy_ (u"ࠣࠤᗶ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢᗷ") + str(target) + bstack11ll1ll_opy_ (u"ࠥࠦᗸ"))
            return None
        instance = TestFramework.bstack1ll11l1ll11_opy_(target)
        if not instance:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡦࡦࡹࡥࡪࡦࡀࡿࡧࡧࡳࡦ࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᗹ") + str(target) + bstack11ll1ll_opy_ (u"ࠧࠨᗺ"))
            return None
        bstack1l1lllllll1_opy_ = TestFramework.get_state(instance, bstack1l11lll1lll_opy_.bstack1ll111lll1l_opy_, {})
        if os.getenv(bstack11ll1ll_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡌࡉ࡙ࡖࡘࡖࡊ࡙ࠢᗻ"), bstack11ll1ll_opy_ (u"ࠢ࠲ࠤᗼ")) == bstack11ll1ll_opy_ (u"ࠣ࠳ࠥᗽ"):
            bstack1ll11l1ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠤ࠽ࠦᗾ").join((scope, fixturename))
            bstack1ll11l11lll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l111l11_opy_ = {
                bstack11ll1ll_opy_ (u"ࠥ࡯ࡪࡿࠢᗿ"): bstack1ll11l1ll1l_opy_,
                bstack11ll1ll_opy_ (u"ࠦࡹࡧࡧࡴࠤᘀ"): bstack1l11lll1lll_opy_.__1ll1l1111ll_opy_(request.node),
                bstack11ll1ll_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࠨᘁ"): fixturedef,
                bstack11ll1ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᘂ"): scope,
                bstack11ll1ll_opy_ (u"ࠢࡵࡻࡳࡩࠧᘃ"): None,
            }
            try:
                if test_hook_state == bstack1lll1ll1ll1_opy_.POST and callable(getattr(args[-1], bstack11ll1ll_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᘄ"), None)):
                    bstack1ll1l111l11_opy_[bstack11ll1ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᘅ")] = TestFramework.bstack1ll1l11lll1_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1ll1ll1_opy_.PRE:
                bstack1ll1l111l11_opy_[bstack11ll1ll_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᘆ")] = uuid4().__str__()
                bstack1ll1l111l11_opy_[bstack1l11lll1lll_opy_.bstack1l1lllll1l1_opy_] = bstack1ll11l11lll_opy_
            elif test_hook_state == bstack1lll1ll1ll1_opy_.POST:
                bstack1ll1l111l11_opy_[bstack1l11lll1lll_opy_.bstack1ll1l111ll1_opy_] = bstack1ll11l11lll_opy_
            if bstack1ll11l1ll1l_opy_ in bstack1l1lllllll1_opy_:
                bstack1l1lllllll1_opy_[bstack1ll11l1ll1l_opy_].update(bstack1ll1l111l11_opy_)
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࠧᘇ") + str(bstack1l1lllllll1_opy_[bstack1ll11l1ll1l_opy_]) + bstack11ll1ll_opy_ (u"ࠧࠨᘈ"))
            else:
                bstack1l1lllllll1_opy_[bstack1ll11l1ll1l_opy_] = bstack1ll1l111l11_opy_
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡷࡨࡵࡰࡦ࠿ࡾࡷࡨࡵࡰࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡁࢀࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࢁࠥࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࠤᘉ") + str(len(bstack1l1lllllll1_opy_)) + bstack11ll1ll_opy_ (u"ࠢࠣᘊ"))
        TestFramework.bstack1lllllll1l1_opy_(instance, bstack1l11lll1lll_opy_.bstack1ll111lll1l_opy_, bstack1l1lllllll1_opy_)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࡾࡰࡪࡴࠨࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠬࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᘋ") + str(instance.ref()) + bstack11ll1ll_opy_ (u"ࠤࠥᘌ"))
        return instance
    def __1l1llllllll_opy_(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        ob = bstack1lll1l1l1ll_opy_(ctx, self.bstack1ll1l11111l_opy_, self.bstack1ll11ll1l11_opy_, test_framework_state)
        TestFramework.bstack1ll11ll1l1l_opy_(ob, {
            TestFramework.bstack1lll1ll11ll_opy_: context.test_framework_name,
            TestFramework.bstack1lll11ll1ll_opy_: context.test_framework_version,
            TestFramework.bstack1ll111l1111_opy_: [],
            bstack1l11lll1lll_opy_.bstack1ll111lll1l_opy_: {},
            bstack1l11lll1lll_opy_.bstack1ll111llll1_opy_: {},
            bstack1l11lll1lll_opy_.bstack1ll11l1111l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllllll1l1_opy_(ob, TestFramework.bstack1l1llll11l1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllllll1l1_opy_(ob, TestFramework.bstack1llll1l11ll_opy_, context.platform_index)
        TestFramework.bstack1llll111111_opy_[ctx.id] = ob
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡨࡺࡸ࠯࡫ࡧࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࡻࡵࡣࡵ࡫ࡪࡺࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᘍ") + str(TestFramework.bstack1llll111111_opy_.keys()) + bstack11ll1ll_opy_ (u"ࠦࠧᘎ"))
        return ob
    def bstack1ll11l111ll_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_]):
        bstack1ll11l11111_opy_ = (
            bstack1l11lll1lll_opy_.bstack1l1lllll11l_opy_
            if bstack1lllllllll1_opy_[1] == bstack1lll1ll1ll1_opy_.PRE
            else bstack1l11lll1lll_opy_.bstack1l1llllll11_opy_
        )
        hook = bstack1l11lll1lll_opy_.bstack1ll11lll11l_opy_(instance, bstack1ll11l11111_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1l111_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll111l1111_opy_, []))
        return entries
    def bstack1ll11lll1ll_opy_(self, instance: bstack1lll1l1l1ll_opy_, bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_]):
        bstack1ll11l11111_opy_ = (
            bstack1l11lll1lll_opy_.bstack1l1lllll11l_opy_
            if bstack1lllllllll1_opy_[1] == bstack1lll1ll1ll1_opy_.PRE
            else bstack1l11lll1lll_opy_.bstack1l1llllll11_opy_
        )
        bstack1l11lll1lll_opy_.bstack1ll11ll1111_opy_(instance, bstack1ll11l11111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll111l1111_opy_, []).clear()
    def bstack1ll11111ll1_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᘏ")
        global _1ll1l1l1l11_opy_
        platform_index = os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᘐ")]
        bstack1ll1111llll_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1l1lll1l1l1_opy_ + str(platform_index)), bstack11lll1l1lll_opy_)
        if not os.path.exists(bstack1ll1111llll_opy_) or not os.path.isdir(bstack1ll1111llll_opy_):
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷࡷࠥࡺ࡯ࠡࡲࡵࡳࡨ࡫ࡳࡴࠢࡾࢁࠧᘑ").format(bstack1ll1111llll_opy_))
            return
        logs = hook.get(bstack11ll1ll_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᘒ"), [])
        with os.scandir(bstack1ll1111llll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1l1l1l11_opy_:
                    self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢᘓ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11ll1ll_opy_ (u"ࠥࠦᘔ")
                    log_entry = bstack1l1llll111l_opy_(
                        kind=bstack11ll1ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᘕ"),
                        message=bstack11ll1ll_opy_ (u"ࠧࠨᘖ"),
                        level=bstack11ll1ll_opy_ (u"ࠨࠢᘗ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1llllll1l_opy_=entry.stat().st_size,
                        bstack1ll111l11l1_opy_=bstack11ll1ll_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᘘ"),
                        bstack1111lll_opy_=os.path.abspath(entry.path),
                        bstack1ll11l1l1ll_opy_=hook.get(TestFramework.bstack1ll1l11l11l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1l1l1l11_opy_.add(abs_path)
        platform_index = os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᘙ")]
        bstack1ll11l111l1_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1l1lll1l1l1_opy_ + str(platform_index)), bstack11lll1l1lll_opy_, bstack11lll1ll111_opy_)
        if not os.path.exists(bstack1ll11l111l1_opy_) or not os.path.isdir(bstack1ll11l111l1_opy_):
            self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡑࡳࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡬࡯ࡶࡰࡧࠤࡦࡺ࠺ࠡࡽࢀࠦᘚ").format(bstack1ll11l111l1_opy_))
        else:
            self.logger.info(bstack11ll1ll_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᘛ").format(bstack1ll11l111l1_opy_))
            with os.scandir(bstack1ll11l111l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1l1l1l11_opy_:
                        self.logger.info(bstack11ll1ll_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᘜ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11ll1ll_opy_ (u"ࠧࠨᘝ")
                        log_entry = bstack1l1llll111l_opy_(
                            kind=bstack11ll1ll_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᘞ"),
                            message=bstack11ll1ll_opy_ (u"ࠢࠣᘟ"),
                            level=bstack11ll1ll_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᘠ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1llllll1l_opy_=entry.stat().st_size,
                            bstack1ll111l11l1_opy_=bstack11ll1ll_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᘡ"),
                            bstack1111lll_opy_=os.path.abspath(entry.path),
                            bstack1ll1l11ll11_opy_=hook.get(TestFramework.bstack1ll1l11l11l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1l1l1l11_opy_.add(abs_path)
        hook[bstack11ll1ll_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᘢ")] = logs
    def bstack1ll1111l111_opy_(
        self,
        bstack1ll111l1l11_opy_: bstack1lll1l1l1ll_opy_,
        entries: List[bstack1l1llll111l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣᘣ"))
        req.platform_index = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1llll1l11ll_opy_)
        req.execution_context.hash = str(bstack1ll111l1l11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111l1l11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111l1l11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll1ll11ll_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll11ll1ll_opy_)
            log_entry.uuid = entry.bstack1ll11l1l1ll_opy_
            log_entry.test_framework_state = bstack1ll111l1l11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11ll1ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᘤ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack11ll1ll_opy_ (u"ࠨࠢᘥ")
            if entry.kind == bstack11ll1ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᘦ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llllll1l_opy_
                log_entry.file_path = entry.bstack1111lll_opy_
        def bstack1l1lll11lll_opy_():
            bstack111111ll11_opy_ = datetime.now()
            try:
                self.bstack1llllll1l1l_opy_.LogCreatedEvent(req)
                bstack1ll111l1l11_opy_.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᘧ"), datetime.now() - bstack111111ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll1ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࢁࡽࠣᘨ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll111llll_opy_.enqueue(bstack1l1lll11lll_opy_)
    def __1ll111111l1_opy_(self, instance) -> None:
        bstack11ll1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡍࡱࡤࡨࡸࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡪࡧࡴࡦࡵࠣࡥࠥࡪࡩࡤࡶࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࡥࠢࡩࡶࡴࡳࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡦࡴࡤࠡࡷࡳࡨࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡵࡷࡥࡹ࡫ࠠࡶࡵ࡬ࡲ࡬ࠦࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᘩ")
        bstack1ll1l1l1111_opy_ = {bstack11ll1ll_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᘪ"): bstack1ll11llll11_opy_.bstack1ll11llll1l_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11ll1l1l_opy_(instance, bstack1ll1l1l1111_opy_)
    @staticmethod
    def bstack1ll11lll11l_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll11l11111_opy_: str):
        bstack1l1llll1l11_opy_ = (
            bstack1l11lll1lll_opy_.bstack1ll111llll1_opy_
            if bstack1ll11l11111_opy_ == bstack1l11lll1lll_opy_.bstack1l1llllll11_opy_
            else bstack1l11lll1lll_opy_.bstack1ll11l1111l_opy_
        )
        bstack1ll11111l1l_opy_ = TestFramework.get_state(instance, bstack1ll11l11111_opy_, None)
        bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1l1llll1l11_opy_, None) if bstack1ll11111l1l_opy_ else None
        return (
            bstack1ll11llllll_opy_[bstack1ll11111l1l_opy_][-1]
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1ll11111l1l_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11ll1111_opy_(instance: bstack1lll1l1l1ll_opy_, bstack1ll11l11111_opy_: str):
        hook = bstack1l11lll1lll_opy_.bstack1ll11lll11l_opy_(instance, bstack1ll11l11111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1l111_opy_, []).clear()
    @staticmethod
    def __1ll111111ll_opy_(instance: bstack1lll1l1l1ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11ll1ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥᘫ"), None)):
            return
        if os.getenv(bstack11ll1ll_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥᘬ"), bstack11ll1ll_opy_ (u"ࠢ࠲ࠤᘭ")) != bstack11ll1ll_opy_ (u"ࠣ࠳ࠥᘮ"):
            bstack1l11lll1lll_opy_.logger.warning(bstack11ll1ll_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦᘯ"))
            return
        bstack1ll111lll11_opy_ = {
            bstack11ll1ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᘰ"): (bstack1l11lll1lll_opy_.bstack1l1lllll11l_opy_, bstack1l11lll1lll_opy_.bstack1ll11l1111l_opy_),
            bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᘱ"): (bstack1l11lll1lll_opy_.bstack1l1llllll11_opy_, bstack1l11lll1lll_opy_.bstack1ll111llll1_opy_),
        }
        for when in (bstack11ll1ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᘲ"), bstack11ll1ll_opy_ (u"ࠨࡣࡢ࡮࡯ࠦᘳ"), bstack11ll1ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᘴ")):
            bstack1l1lllll1ll_opy_ = args[1].get_records(when)
            if not bstack1l1lllll1ll_opy_:
                continue
            records = [
                bstack1l1llll111l_opy_(
                    kind=TestFramework.bstack1ll11111lll_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11ll1ll_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦᘵ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11ll1ll_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥᘶ")) and r.created
                        else None
                    ),
                )
                for r in bstack1l1lllll1ll_opy_
                if isinstance(getattr(r, bstack11ll1ll_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦᘷ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l1llll11ll_opy_, bstack1l1llll1l11_opy_ = bstack1ll111lll11_opy_.get(when, (None, None))
            bstack1ll11l11l11_opy_ = TestFramework.get_state(instance, bstack1l1llll11ll_opy_, None) if bstack1l1llll11ll_opy_ else None
            bstack1ll11llllll_opy_ = TestFramework.get_state(instance, bstack1l1llll1l11_opy_, None) if bstack1ll11l11l11_opy_ else None
            if isinstance(bstack1ll11llllll_opy_, dict) and len(bstack1ll11llllll_opy_.get(bstack1ll11l11l11_opy_, [])) > 0:
                hook = bstack1ll11llllll_opy_[bstack1ll11l11l11_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1l111_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1l111_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll111l1111_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1111ll1l_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11lll1lll_opy_.__1ll11ll111l_opy_(test.location) if hasattr(test, bstack11ll1ll_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᘸ")) else getattr(test, bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᘹ"), None)
        test_name = test.name if hasattr(test, bstack11ll1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᘺ")) else None
        bstack1ll111l11ll_opy_ = test.fspath.strpath if hasattr(test, bstack11ll1ll_opy_ (u"ࠢࡧࡵࡳࡥࡹ࡮ࠢᘻ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll111l11ll_opy_:
            return None
        code = None
        if hasattr(test, bstack11ll1ll_opy_ (u"ࠣࡱࡥ࡮ࠧᘼ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11lll1ll11l_opy_ = []
        try:
            bstack11lll1ll11l_opy_ = bstack1l11l1l1_opy_.bstack1l111111_opy_(test)
        except:
            bstack1l11lll1lll_opy_.logger.warning(bstack11ll1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸࡪࡹࡴࠡࡵࡦࡳࡵ࡫ࡳ࠭ࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡴࡨࡷࡴࡲࡶࡦࡦࠣ࡭ࡳࠦࡃࡍࡋࠥᘽ"))
        return {
            TestFramework.bstack1lll11llll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11llll_opy_: test_id,
            TestFramework.bstack1ll11ll11l1_opy_: test_name,
            TestFramework.bstack1ll111ll11l_opy_: getattr(test, bstack11ll1ll_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᘾ"), None),
            TestFramework.bstack1ll1111l1l1_opy_: bstack1ll111l11ll_opy_,
            TestFramework.bstack1ll111l111l_opy_: bstack1l11lll1lll_opy_.__1ll1l1111ll_opy_(test),
            TestFramework.bstack1l1llll1111_opy_: code,
            TestFramework.bstack1llll1111l1_opy_: TestFramework.bstack1l1lll1lll1_opy_,
            TestFramework.bstack1ll1lllll11_opy_: test_id,
            TestFramework.bstack1l11111111l_opy_: bstack11lll1ll11l_opy_
        }
    @staticmethod
    def __1ll1l1111ll_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack11ll1ll_opy_ (u"ࠦࡴࡽ࡮ࡠ࡯ࡤࡶࡰ࡫ࡲࡴࠤᘿ"), [])
            markers.extend([getattr(m, bstack11ll1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᙀ"), None) for m in own_markers if getattr(m, bstack11ll1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᙁ"), None)])
            current = getattr(current, bstack11ll1ll_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᙂ"), None)
        return markers
    @staticmethod
    def __1ll11ll111l_opy_(location):
        return bstack11ll1ll_opy_ (u"ࠣ࠼࠽ࠦᙃ").join(filter(lambda x: isinstance(x, str), location))