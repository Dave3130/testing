# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1ll1llll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1ll1l11_opy_ import bstack1ll11l1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1l1ll1l_opy_,
    bstack1llll1l1l11_opy_,
    bstack1lll1llll1l_opy_,
    bstack1ll11l111ll_opy_,
    bstack1ll111l1l1l_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll111l11l1_opy_
from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1l1lllll111_opy_ import bstack1ll11l111l1_opy_
from bstack_utils.bstack1ll111l1_opy_ import bstack11lll1l1_opy_
bstack1ll11ll1l1l_opy_ = bstack1ll111l11l1_opy_()
bstack1l1llllllll_opy_ = 1.0
bstack1ll111ll111_opy_ = bstack1l_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥᕬ")
bstack11llll1llll_opy_ = bstack1l_opy_ (u"࡙ࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢᕭ")
bstack11llll1l1ll_opy_ = bstack1l_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᕮ")
bstack11llll1ll1l_opy_ = bstack1l_opy_ (u"ࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤᕯ")
bstack11llll1lll1_opy_ = bstack1l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨᕰ")
_1ll11l1l1ll_opy_ = set()
class bstack1l1l1l111ll_opy_(TestFramework):
    bstack1ll1l11l11l_opy_ = bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᕱ")
    bstack1ll11l11l11_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࠢᕲ")
    bstack1ll11l11l1l_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᕳ")
    bstack1ll11l11ll1_opy_ = bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࠨᕴ")
    bstack1ll11l1l11l_opy_ = bstack1l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᕵ")
    bstack1ll1111l111_opy_: bool
    bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_  = None
    bstack1llll1lll1l_opy_ = None
    bstack1ll1l1ll1l1_opy_ = [
        bstack1lll1l1ll1l_opy_.BEFORE_ALL,
        bstack1lll1l1ll1l_opy_.AFTER_ALL,
        bstack1lll1l1ll1l_opy_.BEFORE_EACH,
        bstack1lll1l1ll1l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11ll11l1_opy_: Dict[str, str],
        bstack1ll11l1llll_opy_: List[str]=[bstack1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᕶ")],
        bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_=None,
        bstack1llll1lll1l_opy_=None
    ):
        super().__init__(bstack1ll11l1llll_opy_, bstack1ll11ll11l1_opy_, bstack1lll1l11111_opy_)
        self.bstack1ll1111l111_opy_ = any(bstack1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᕷ") in item.lower() for item in bstack1ll11l1llll_opy_)
        self.bstack1llll1lll1l_opy_ = bstack1llll1lll1l_opy_
    def track_event(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1l1ll1l_opy_.TEST or test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1l1ll1l1_opy_:
            bstack1ll11l1ll11_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1l1ll1l_opy_.NONE:
            self.logger.warning(bstack1l_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࠤᕸ") + str(test_hook_state) + bstack1l_opy_ (u"ࠤࠥᕹ"))
            return
        if not self.bstack1ll1111l111_opy_:
            self.logger.warning(bstack1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡀࠦᕺ") + str(str(self.bstack1ll11l1llll_opy_)) + bstack1l_opy_ (u"ࠦࠧᕻ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕼ") + str(kwargs) + bstack1l_opy_ (u"ࠨࠢᕽ"))
            return
        instance = self.__1ll11111l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡢࡴࡪࡷࡂࠨᕾ") + str(args) + bstack1l_opy_ (u"ࠣࠤᕿ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1l1ll1l1_opy_ and test_hook_state == bstack1lll1llll1l_opy_.PRE:
                bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1lll11l1l_opy_.value)
                name = str(EVENTS.bstack1lll11l1l_opy_.name)+bstack1l_opy_ (u"ࠤ࠽ࠦᖀ")+str(test_framework_state.name)
                TestFramework.bstack1ll1111ll11_opy_(instance, name, bstack1ll1l1lll11_opy_)
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࠦࡰࡳࡧ࠽ࠤࢀࢃࠢᖁ").format(e))
        try:
            if not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_) and test_hook_state == bstack1lll1llll1l_opy_.PRE:
                test = bstack1l1l1l111ll_opy_.__1ll1l111l1l_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1l_opy_ (u"ࠦࡱࡵࡡࡥࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᖂ") + str(test_hook_state) + bstack1l_opy_ (u"ࠧࠨᖃ"))
            if test_framework_state == bstack1lll1l1ll1l_opy_.TEST:
                if test_hook_state == bstack1lll1llll1l_opy_.PRE and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_):
                    TestFramework.bstack1lllll11ll1_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡵࡷࡥࡷࡺࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᖄ") + str(test_hook_state) + bstack1l_opy_ (u"ࠢࠣᖅ"))
                elif test_hook_state == bstack1lll1llll1l_opy_.POST and not TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1ll11111_opy_):
                    TestFramework.bstack1lllll11ll1_opy_(instance, TestFramework.bstack1ll1ll11111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡩࡳࡪࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᖆ") + str(test_hook_state) + bstack1l_opy_ (u"ࠤࠥᖇ"))
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG and test_hook_state == bstack1lll1llll1l_opy_.POST:
                bstack1l1l1l111ll_opy_.__1ll1l1111l1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG_REPORT and test_hook_state == bstack1lll1llll1l_opy_.POST:
                self.__1ll11lll11l_opy_(instance, *args)
                self.__1ll1l11ll11_opy_(instance)
            elif test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1l1ll1l1_opy_:
                self.__1ll1l1l1111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᖈ") + str(instance.ref()) + bstack1l_opy_ (u"ࠦࠧᖉ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1111ll1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l1l111ll_opy_.bstack1ll1l1ll1l1_opy_ and test_hook_state == bstack1lll1llll1l_opy_.POST:
                name = str(EVENTS.bstack1lll11l1l_opy_.name)+bstack1l_opy_ (u"ࠧࡀࠢᖊ")+str(test_framework_state.name)
                bstack1ll1l1lll11_opy_ = TestFramework.bstack1ll11llll1l_opy_(instance, name)
                bstack1llll1l1lll_opy_.end(EVENTS.bstack1lll11l1l_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᖋ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᖌ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᖍ").format(e))
    def bstack1ll111lll11_opy_(self):
        return self.bstack1ll1111l111_opy_
    def __1ll11l1111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨᖎ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l1ll1_opy_(rep, [bstack1l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᖏ"), bstack1l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᖐ"), bstack1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧᖑ"), bstack1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᖒ"), bstack1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠣᖓ"), bstack1l_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢᖔ")])
        return None
    def __1ll11lll11l_opy_(self, instance: bstack1llll1l1l11_opy_, *args):
        result = self.__1ll11l1111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l11ll_opy_ = None
        if result.get(bstack1l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖕ"), None) == bstack1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᖖ") and len(args) > 1 and getattr(args[1], bstack1l_opy_ (u"ࠦࡪࡾࡣࡪࡰࡩࡳࠧᖗ"), None) is not None:
            failure = [{bstack1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᖘ"): [args[1].excinfo.exconly(), result.get(bstack1l_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᖙ"), None)]}]
            bstack11111l11ll_opy_ = bstack1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᖚ") if bstack1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᖛ") in getattr(args[1].excinfo, bstack1l_opy_ (u"ࠤࡷࡽࡵ࡫࡮ࡢ࡯ࡨࠦᖜ"), bstack1l_opy_ (u"ࠥࠦᖝ")) else bstack1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᖞ")
        bstack1ll1111l1l1_opy_ = result.get(bstack1l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᖟ"), TestFramework.bstack1ll111l1l11_opy_)
        if bstack1ll1111l1l1_opy_ != TestFramework.bstack1ll111l1l11_opy_:
            TestFramework.bstack1lllll11ll1_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11111111_opy_(instance, {
            TestFramework.bstack1lll1lll1l1_opy_: failure,
            TestFramework.bstack1ll1l1ll111_opy_: bstack11111l11ll_opy_,
            TestFramework.bstack1lll1ll1lll_opy_: bstack1ll1111l1l1_opy_,
        })
    def __1ll11111l1l_opy_(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1l1ll1l_opy_.SETUP_FIXTURE:
            instance = self.__1ll11ll111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11ll11ll_opy_ bstack1ll1l11ll1l_opy_ this to be bstack1l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖠ")
            if test_framework_state == bstack1lll1l1ll1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11l1ll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᖡ"), None), bstack1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᖢ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᖣ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11ll1ll1_opy_(target) if target else None
        return instance
    def __1ll1l1l1111_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1111lll1_opy_ = TestFramework.get_state(instance, bstack1l1l1l111ll_opy_.bstack1ll11l11l11_opy_, {})
        if not key in bstack1ll1111lll1_opy_:
            bstack1ll1111lll1_opy_[key] = []
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, bstack1l1l1l111ll_opy_.bstack1ll11l11l1l_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll11lll1l1_opy_ = {
            bstack1l1l1l111ll_opy_.bstack1ll11l11l11_opy_: bstack1ll1111lll1_opy_,
            bstack1l1l1l111ll_opy_.bstack1ll11l11l1l_opy_: bstack1l1llllll11_opy_,
        }
        if test_hook_state == bstack1lll1llll1l_opy_.PRE:
            hook = {
                bstack1l_opy_ (u"ࠥ࡯ࡪࡿࠢᖤ"): key,
                TestFramework.bstack1ll1l1llll1_opy_: uuid4().__str__(),
                TestFramework.bstack1ll1l11l1l1_opy_: TestFramework.bstack1ll111lllll_opy_,
                TestFramework.bstack1ll1l111lll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1l1lll1l_opy_: [],
                TestFramework.bstack1ll11llll11_opy_: args[1] if len(args) > 1 else bstack1l_opy_ (u"ࠫࠬᖥ"),
                TestFramework.bstack1ll11ll1lll_opy_: bstack1ll11l111l1_opy_.bstack1ll11lllll1_opy_()
            }
            bstack1ll1111lll1_opy_[key].append(hook)
            bstack1ll11lll1l1_opy_[bstack1l1l1l111ll_opy_.bstack1ll11l11ll1_opy_] = key
        elif test_hook_state == bstack1lll1llll1l_opy_.POST:
            bstack1ll111l111l_opy_ = bstack1ll1111lll1_opy_.get(key, [])
            hook = bstack1ll111l111l_opy_.pop() if bstack1ll111l111l_opy_ else None
            if hook:
                result = self.__1ll11l1111l_opy_(*args)
                if result:
                    bstack1ll1l1l1lll_opy_ = result.get(bstack1l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᖦ"), TestFramework.bstack1ll111lllll_opy_)
                    if bstack1ll1l1l1lll_opy_ != TestFramework.bstack1ll111lllll_opy_:
                        hook[TestFramework.bstack1ll1l11l1l1_opy_] = bstack1ll1l1l1lll_opy_
                hook[TestFramework.bstack1ll111111ll_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11ll1lll_opy_]= bstack1ll11l111l1_opy_.bstack1ll11lllll1_opy_()
                self.bstack1l1llll1lll_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll1l111l11_opy_, [])
                if logs: self.bstack1ll1111l11l_opy_(instance, logs)
                bstack1l1llllll11_opy_[key].append(hook)
                bstack1ll11lll1l1_opy_[bstack1l1l1l111ll_opy_.bstack1ll11l1l11l_opy_] = key
        TestFramework.bstack1ll11111111_opy_(instance, bstack1ll11lll1l1_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡮࡯ࡰ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁ࡫ࡦࡻࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤ࠾ࡽ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡁࠧᖧ") + str(bstack1l1llllll11_opy_) + bstack1l_opy_ (u"ࠢࠣᖨ"))
    def __1ll11ll111l_opy_(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l1ll1_opy_(args[0], [bstack1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᖩ"), bstack1l_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥᖪ"), bstack1l_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᖫ"), bstack1l_opy_ (u"ࠦ࡮ࡪࡳࠣᖬ"), bstack1l_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢᖭ"), bstack1l_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨᖮ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᖯ")) else fixturedef.get(bstack1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᖰ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢᖱ")) else None
        node = request.node if hasattr(request, bstack1l_opy_ (u"ࠥࡲࡴࡪࡥࠣᖲ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᖳ")) else None
        baseid = fixturedef.get(bstack1l_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧᖴ"), None) or bstack1l_opy_ (u"ࠨࠢᖵ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l_opy_ (u"ࠢࡠࡲࡼࡪࡺࡴࡣࡪࡶࡨࡱࠧᖶ")):
            target = bstack1l1l1l111ll_opy_.__1ll1l1l11ll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥᖷ")) else None
            if target and not TestFramework.bstack1ll11ll1ll1_opy_(target):
                self.__1ll1l11l1ll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡳࡵࡤࡦ࠿ࡾࡲࡴࡪࡥࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᖸ") + str(test_hook_state) + bstack1l_opy_ (u"ࠥࠦᖹ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤᖺ") + str(target) + bstack1l_opy_ (u"ࠧࠨᖻ"))
            return None
        instance = TestFramework.bstack1ll11ll1ll1_opy_(target)
        if not instance:
            self.logger.warning(bstack1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡨࡡࡴࡧ࡬ࡨࡂࢁࡢࡢࡵࡨ࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣᖼ") + str(target) + bstack1l_opy_ (u"ࠢࠣᖽ"))
            return None
        bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, bstack1l1l1l111ll_opy_.bstack1ll1l11l11l_opy_, {})
        if os.getenv(bstack1l_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡇࡋ࡛ࡘ࡚ࡘࡅࡔࠤᖾ"), bstack1l_opy_ (u"ࠤ࠴ࠦᖿ")) == bstack1l_opy_ (u"ࠥ࠵ࠧᗀ"):
            bstack1ll1l1l1l11_opy_ = bstack1l_opy_ (u"ࠦ࠿ࠨᗁ").join((scope, fixturename))
            bstack1ll1l1ll11l_opy_ = datetime.now(tz=timezone.utc)
            bstack1l1lllll1ll_opy_ = {
                bstack1l_opy_ (u"ࠧࡱࡥࡺࠤᗂ"): bstack1ll1l1l1l11_opy_,
                bstack1l_opy_ (u"ࠨࡴࡢࡩࡶࠦᗃ"): bstack1l1l1l111ll_opy_.__1ll11lll111_opy_(request.node),
                bstack1l_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࠣᗄ"): fixturedef,
                bstack1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᗅ"): scope,
                bstack1l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᗆ"): None,
            }
            try:
                if test_hook_state == bstack1lll1llll1l_opy_.POST and callable(getattr(args[-1], bstack1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᗇ"), None)):
                    bstack1l1lllll1ll_opy_[bstack1l_opy_ (u"ࠦࡹࡿࡰࡦࠤᗈ")] = TestFramework.bstack1ll1l111111_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1llll1l_opy_.PRE:
                bstack1l1lllll1ll_opy_[bstack1l_opy_ (u"ࠧࡻࡵࡪࡦࠥᗉ")] = uuid4().__str__()
                bstack1l1lllll1ll_opy_[bstack1l1l1l111ll_opy_.bstack1ll1l111lll_opy_] = bstack1ll1l1ll11l_opy_
            elif test_hook_state == bstack1lll1llll1l_opy_.POST:
                bstack1l1lllll1ll_opy_[bstack1l1l1l111ll_opy_.bstack1ll111111ll_opy_] = bstack1ll1l1ll11l_opy_
            if bstack1ll1l1l1l11_opy_ in bstack1ll11l1lll1_opy_:
                bstack1ll11l1lll1_opy_[bstack1ll1l1l1l11_opy_].update(bstack1l1lllll1ll_opy_)
                self.logger.debug(bstack1l_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࠢᗊ") + str(bstack1ll11l1lll1_opy_[bstack1ll1l1l1l11_opy_]) + bstack1l_opy_ (u"ࠢࠣᗋ"))
            else:
                bstack1ll11l1lll1_opy_[bstack1ll1l1l1l11_opy_] = bstack1l1lllll1ll_opy_
                self.logger.debug(bstack1l_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࢃࠠࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࠦᗌ") + str(len(bstack1ll11l1lll1_opy_)) + bstack1l_opy_ (u"ࠤࠥᗍ"))
        TestFramework.bstack1lllll11ll1_opy_(instance, bstack1l1l1l111ll_opy_.bstack1ll1l11l11l_opy_, bstack1ll11l1lll1_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࢀࡲࡥ࡯ࠪࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷ࠮ࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᗎ") + str(instance.ref()) + bstack1l_opy_ (u"ࠦࠧᗏ"))
        return instance
    def __1ll1l11l1ll_opy_(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1llll_opy_.create_context(target)
        ob = bstack1llll1l1l11_opy_(ctx, self.bstack1ll11l1llll_opy_, self.bstack1ll11ll11l1_opy_, test_framework_state)
        TestFramework.bstack1ll11111111_opy_(ob, {
            TestFramework.bstack1llll11111l_opy_: context.test_framework_name,
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l11111l_opy_: [],
            bstack1l1l1l111ll_opy_.bstack1ll1l11l11l_opy_: {},
            bstack1l1l1l111ll_opy_.bstack1ll11l11l1l_opy_: {},
            bstack1l1l1l111ll_opy_.bstack1ll11l11l11_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll11ll1_opy_(ob, TestFramework.bstack1ll111l1ll1_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll11ll1_opy_(ob, TestFramework.bstack1llll1lllll_opy_, context.platform_index)
        TestFramework.bstack1llll11l1ll_opy_[ctx.id] = ob
        self.logger.debug(bstack1l_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡣࡵࡺ࠱࡭ࡩࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᗐ") + str(TestFramework.bstack1llll11l1ll_opy_.keys()) + bstack1l_opy_ (u"ࠨࠢᗑ"))
        return ob
    def bstack1ll1l111ll1_opy_(self, instance: bstack1llll1l1l11_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_]):
        bstack1ll111l1lll_opy_ = (
            bstack1l1l1l111ll_opy_.bstack1ll11l11ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll1llll1l_opy_.PRE
            else bstack1l1l1l111ll_opy_.bstack1ll11l1l11l_opy_
        )
        hook = bstack1l1l1l111ll_opy_.bstack1ll11l1ll1l_opy_(instance, bstack1ll111l1lll_opy_)
        entries = hook.get(TestFramework.bstack1ll1l1lll1l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l11111l_opy_, []))
        return entries
    def bstack1ll111llll1_opy_(self, instance: bstack1llll1l1l11_opy_, bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_]):
        bstack1ll111l1lll_opy_ = (
            bstack1l1l1l111ll_opy_.bstack1ll11l11ll1_opy_
            if bstack1lllll1ll11_opy_[1] == bstack1lll1llll1l_opy_.PRE
            else bstack1l1l1l111ll_opy_.bstack1ll11l1l11l_opy_
        )
        bstack1l1l1l111ll_opy_.bstack1ll11l1l111_opy_(instance, bstack1ll111l1lll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l11111l_opy_, []).clear()
    def bstack1l1llll1lll_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡹࡩ࡮࡫࡯ࡥࡷࠦࡴࡰࠢࡷ࡬ࡪࠦࡊࡢࡸࡤࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪ࡬ࡷࠥࡳࡥࡵࡪࡲࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡈ࡮ࡥࡤ࡭ࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡇࡱࡵࠤࡪࡧࡣࡩࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸ࠲ࠠࡳࡧࡳࡰࡦࡩࡥࡴࠢࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤࠣ࡭ࡳࠦࡩࡵࡵࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡊࡨࠣࡥࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡩࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡭ࡢࡶࡦ࡬ࡪࡹࠠࡢࠢࡰࡳࡩ࡯ࡦࡪࡧࡧࠤ࡭ࡵ࡯࡬࠯࡯ࡩࡻ࡫࡬ࠡࡨ࡬ࡰࡪ࠲ࠠࡪࡶࠣࡧࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࠡࡹ࡬ࡸ࡭ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡗ࡮ࡳࡩ࡭ࡣࡵࡰࡾ࠲ࠠࡪࡶࠣࡴࡷࡵࡣࡦࡵࡶࡩࡸࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡ࡮ࡲࡧࡦࡺࡥࡥࠢ࡬ࡲࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡣࡻࠣࡶࡪࡶ࡬ࡢࡥ࡬ࡲ࡬ࠦࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡔࡩࡧࠣࡧࡷ࡫ࡡࡵࡧࡧࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡢࡴࡨࠤࡦࡪࡤࡦࡦࠣࡸࡴࠦࡴࡩࡧࠣ࡬ࡴࡵ࡫ࠨࡵࠣࠦࡱࡵࡧࡴࠤࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯࠿ࠦࡔࡩࡧࠣࡩࡻ࡫࡮ࡵࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵࠣࡥࡳࡪࠠࡩࡱࡲ࡯ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᗒ")
        global _1ll11l1l1ll_opy_
        platform_index = os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᗓ")]
        bstack1ll1l1l11l1_opy_ = os.path.join(bstack1ll11ll1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack11llll1ll1l_opy_)
        if not os.path.exists(bstack1ll1l1l11l1_opy_) or not os.path.isdir(bstack1ll1l1l11l1_opy_):
            self.logger.debug(bstack1l_opy_ (u"ࠤࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡹࠠࡵࡱࠣࡴࡷࡵࡣࡦࡵࡶࠤࢀࢃࠢᗔ").format(bstack1ll1l1l11l1_opy_))
            return
        logs = hook.get(bstack1l_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᗕ"), [])
        with os.scandir(bstack1ll1l1l11l1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l1l1ll_opy_:
                    self.logger.info(bstack1l_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᗖ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l_opy_ (u"ࠧࠨᗗ")
                    log_entry = bstack1ll111l1l1l_opy_(
                        kind=bstack1l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᗘ"),
                        message=bstack1l_opy_ (u"ࠢࠣᗙ"),
                        level=bstack1l_opy_ (u"ࠣࠤᗚ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll111ll1l1_opy_=entry.stat().st_size,
                        bstack1ll1l11l111_opy_=bstack1l_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᗛ"),
                        bstack1ll11l1_opy_=os.path.abspath(entry.path),
                        bstack1l1lllll11l_opy_=hook.get(TestFramework.bstack1ll1l1llll1_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l1l1ll_opy_.add(abs_path)
        platform_index = os.environ[bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᗜ")]
        bstack1l1llllll1l_opy_ = os.path.join(bstack1ll11ll1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), bstack11llll1ll1l_opy_, bstack11llll1lll1_opy_)
        if not os.path.exists(bstack1l1llllll1l_opy_) or not os.path.isdir(bstack1l1llllll1l_opy_):
            self.logger.info(bstack1l_opy_ (u"ࠦࡓࡵࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡧࡱࡸࡲࡩࠦࡡࡵ࠼ࠣࡿࢂࠨᗝ").format(bstack1l1llllll1l_opy_))
        else:
            self.logger.info(bstack1l_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡦࡳࡱࡰࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦᗞ").format(bstack1l1llllll1l_opy_))
            with os.scandir(bstack1l1llllll1l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l1l1ll_opy_:
                        self.logger.info(bstack1l_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦᗟ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l_opy_ (u"ࠢࠣᗠ")
                        log_entry = bstack1ll111l1l1l_opy_(
                            kind=bstack1l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᗡ"),
                            message=bstack1l_opy_ (u"ࠤࠥᗢ"),
                            level=bstack1l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᗣ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll111ll1l1_opy_=entry.stat().st_size,
                            bstack1ll1l11l111_opy_=bstack1l_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᗤ"),
                            bstack1ll11l1_opy_=os.path.abspath(entry.path),
                            bstack1ll11ll1l11_opy_=hook.get(TestFramework.bstack1ll1l1llll1_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l1l1ll_opy_.add(abs_path)
        hook[bstack1l_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᗥ")] = logs
    def bstack1ll1111l11l_opy_(
        self,
        bstack1l1lllll1l1_opy_: bstack1llll1l1l11_opy_,
        entries: List[bstack1ll111l1l1l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡓࡆࡕࡖࡍࡔࡔ࡟ࡊࡆࠥᗦ"))
        req.platform_index = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll1lllll_opy_)
        req.execution_context.hash = str(bstack1l1lllll1l1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1lllll1l1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1lllll1l1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll11111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.uuid = entry.bstack1l1lllll11l_opy_
            log_entry.test_framework_state = bstack1l1lllll1l1_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᗧ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1l_opy_ (u"ࠣࠤᗨ")
            if entry.kind == bstack1l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᗩ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111ll1l1_opy_
                log_entry.file_path = entry.bstack1ll11l1_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1111lll_opy_ = datetime.now()
            try:
                self.bstack1llll1lll1l_opy_.LogCreatedEvent(req)
                bstack1l1lllll1l1_opy_.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢᗪ"), datetime.now() - bstack1l1111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡼࡿࠥᗫ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def __1ll1l11ll11_opy_(self, instance) -> None:
        bstack1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡏࡳࡦࡪࡳࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡸࡥࡢࡶࡨࡷࠥࡧࠠࡥ࡫ࡦࡸࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡡ࡯ࡦࠣࡹࡵࡪࡡࡵࡧࡶࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡷࡹࡧࡴࡦࠢࡸࡷ࡮ࡴࡧࠡࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᗬ")
        bstack1ll11lll1l1_opy_ = {bstack1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣᗭ"): bstack1ll11l111l1_opy_.bstack1ll11lllll1_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll11111111_opy_(instance, bstack1ll11lll1l1_opy_)
    @staticmethod
    def bstack1ll11l1ll1l_opy_(instance: bstack1llll1l1l11_opy_, bstack1ll111l1lll_opy_: str):
        bstack1ll111l1111_opy_ = (
            bstack1l1l1l111ll_opy_.bstack1ll11l11l1l_opy_
            if bstack1ll111l1lll_opy_ == bstack1l1l1l111ll_opy_.bstack1ll11l1l11l_opy_
            else bstack1l1l1l111ll_opy_.bstack1ll11l11l11_opy_
        )
        bstack1ll111111l1_opy_ = TestFramework.get_state(instance, bstack1ll111l1lll_opy_, None)
        bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, bstack1ll111l1111_opy_, None) if bstack1ll111111l1_opy_ else None
        return (
            bstack1ll1l1ll1ll_opy_[bstack1ll111111l1_opy_][-1]
            if isinstance(bstack1ll1l1ll1ll_opy_, dict) and len(bstack1ll1l1ll1ll_opy_.get(bstack1ll111111l1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11l1l111_opy_(instance: bstack1llll1l1l11_opy_, bstack1ll111l1lll_opy_: str):
        hook = bstack1l1l1l111ll_opy_.bstack1ll11l1ll1l_opy_(instance, bstack1ll111l1lll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1l1lll1l_opy_, []).clear()
    @staticmethod
    def __1ll1l1111l1_opy_(instance: bstack1llll1l1l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡣࡰࡴࡧࡷࠧᗮ"), None)):
            return
        if os.getenv(bstack1l_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡍࡑࡊࡗࠧᗯ"), bstack1l_opy_ (u"ࠤ࠴ࠦᗰ")) != bstack1l_opy_ (u"ࠥ࠵ࠧᗱ"):
            bstack1l1l1l111ll_opy_.logger.warning(bstack1l_opy_ (u"ࠦ࡮࡭࡮ࡰࡴ࡬ࡲ࡬ࠦࡣࡢࡲ࡯ࡳ࡬ࠨᗲ"))
            return
        bstack1ll111lll1l_opy_ = {
            bstack1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᗳ"): (bstack1l1l1l111ll_opy_.bstack1ll11l11ll1_opy_, bstack1l1l1l111ll_opy_.bstack1ll11l11l11_opy_),
            bstack1l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᗴ"): (bstack1l1l1l111ll_opy_.bstack1ll11l1l11l_opy_, bstack1l1l1l111ll_opy_.bstack1ll11l11l1l_opy_),
        }
        for when in (bstack1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᗵ"), bstack1l_opy_ (u"ࠣࡥࡤࡰࡱࠨᗶ"), bstack1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᗷ")):
            bstack1ll11ll1111_opy_ = args[1].get_records(when)
            if not bstack1ll11ll1111_opy_:
                continue
            records = [
                bstack1ll111l1l1l_opy_(
                    kind=TestFramework.bstack1ll11111l11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࡰࡤࡱࡪࠨᗸ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࠧᗹ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11ll1111_opy_
                if isinstance(getattr(r, bstack1l_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨᗺ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111ll1ll_opy_, bstack1ll111l1111_opy_ = bstack1ll111lll1l_opy_.get(when, (None, None))
            bstack1ll11111lll_opy_ = TestFramework.get_state(instance, bstack1ll111ll1ll_opy_, None) if bstack1ll111ll1ll_opy_ else None
            bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, bstack1ll111l1111_opy_, None) if bstack1ll11111lll_opy_ else None
            if isinstance(bstack1ll1l1ll1ll_opy_, dict) and len(bstack1ll1l1ll1ll_opy_.get(bstack1ll11111lll_opy_, [])) > 0:
                hook = bstack1ll1l1ll1ll_opy_[bstack1ll11111lll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1l1lll1l_opy_ in hook:
                    hook[TestFramework.bstack1ll1l1lll1l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l11111l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l111l1l_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l1l111ll_opy_.__1ll1l1l11ll_opy_(test.location) if hasattr(test, bstack1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᗻ")) else getattr(test, bstack1l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᗼ"), None)
        test_name = test.name if hasattr(test, bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᗽ")) else None
        bstack1ll111ll11l_opy_ = test.fspath.strpath if hasattr(test, bstack1l_opy_ (u"ࠤࡩࡷࡵࡧࡴࡩࠤᗾ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll111ll11l_opy_:
            return None
        code = None
        if hasattr(test, bstack1l_opy_ (u"ࠥࡳࡧࡰࠢᗿ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll1ll11_opy_ = []
        try:
            bstack11llll1ll11_opy_ = bstack11lll1l1_opy_.bstack1lll1lll_opy_(test)
        except:
            bstack1l1l1l111ll_opy_.logger.warning(bstack1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡥࡴࡶࠣࡷࡨࡵࡰࡦࡵ࠯ࠤࡹ࡫ࡳࡵࠢࡶࡧࡴࡶࡥࡴࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡶࡪࡹ࡯࡭ࡸࡨࡨࠥ࡯࡮ࠡࡅࡏࡍࠧᘀ"))
        return {
            TestFramework.bstack1llll11ll11_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1111ll_opy_: test_id,
            TestFramework.bstack1ll1l11lll1_opy_: test_name,
            TestFramework.bstack1ll1111l1ll_opy_: getattr(test, bstack1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᘁ"), None),
            TestFramework.bstack1ll11l11111_opy_: bstack1ll111ll11l_opy_,
            TestFramework.bstack1ll11lll1ll_opy_: bstack1l1l1l111ll_opy_.__1ll11lll111_opy_(test),
            TestFramework.bstack1ll1ll11l11_opy_: code,
            TestFramework.bstack1lll1ll1lll_opy_: TestFramework.bstack1ll111l1l11_opy_,
            TestFramework.bstack1lll11lll1l_opy_: test_id,
            TestFramework.bstack1l1111l11ll_opy_: bstack11llll1ll11_opy_
        }
    @staticmethod
    def __1ll11lll111_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1l_opy_ (u"ࠨ࡯ࡸࡰࡢࡱࡦࡸ࡫ࡦࡴࡶࠦᘂ"), [])
            markers.extend([getattr(m, bstack1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᘃ"), None) for m in own_markers if getattr(m, bstack1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᘄ"), None)])
            current = getattr(current, bstack1l_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᘅ"), None)
        return markers
    @staticmethod
    def __1ll1l1l11ll_opy_(location):
        return bstack1l_opy_ (u"ࠥ࠾࠿ࠨᘆ").join(filter(lambda x: isinstance(x, str), location))