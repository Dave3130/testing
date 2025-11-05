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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1llll111l1l_opy_, bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1lll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l111l1_opy_, bstack1lll1l1l1ll_opy_, bstack1lll1ll1ll1_opy_, bstack1l1llll111l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll11lll11_opy_, bstack1ll1l1l11l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1ll1ll_opy_ = [bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᏤ"), bstack11ll1ll_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᏥ"), bstack11ll1ll_opy_ (u"ࠧࡩ࡯࡯ࡨ࡬࡫ࠧᏦ"), bstack11ll1ll_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࠢᏧ"), bstack11ll1ll_opy_ (u"ࠢࡱࡣࡷ࡬ࠧᏨ")]
bstack1ll111l1l1l_opy_ = bstack1ll1l1l11l1_opy_()
bstack1l1lll1l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᏩ")
bstack1l111lll1l1_opy_ = {
    bstack11ll1ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡌࡸࡪࡳࠢᏪ"): bstack1l11l1ll1ll_opy_,
    bstack11ll1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡔࡦࡩ࡫ࡢࡩࡨࠦᏫ"): bstack1l11l1ll1ll_opy_,
    bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡒࡵࡤࡶ࡮ࡨࠦᏬ"): bstack1l11l1ll1ll_opy_,
    bstack11ll1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡉ࡬ࡢࡵࡶࠦᏭ"): bstack1l11l1ll1ll_opy_,
    bstack11ll1ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡆࡶࡰࡦࡸ࡮ࡵ࡮ࠣᏮ"): bstack1l11l1ll1ll_opy_
    + [
        bstack11ll1ll_opy_ (u"ࠢࡰࡴ࡬࡫࡮ࡴࡡ࡭ࡰࡤࡱࡪࠨᏯ"),
        bstack11ll1ll_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᏰ"),
        bstack11ll1ll_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧ࡬ࡲ࡫ࡵࠢᏱ"),
        bstack11ll1ll_opy_ (u"ࠥ࡯ࡪࡿࡷࡰࡴࡧࡷࠧᏲ"),
        bstack11ll1ll_opy_ (u"ࠦࡨࡧ࡬࡭ࡵࡳࡩࡨࠨᏳ"),
        bstack11ll1ll_opy_ (u"ࠧࡩࡡ࡭࡮ࡲࡦ࡯ࠨᏴ"),
        bstack11ll1ll_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧᏵ"),
        bstack11ll1ll_opy_ (u"ࠢࡴࡶࡲࡴࠧ᏶"),
        bstack11ll1ll_opy_ (u"ࠣࡦࡸࡶࡦࡺࡩࡰࡰࠥ᏷"),
        bstack11ll1ll_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᏸ"),
    ],
    bstack11ll1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦ࡯࡮࠯ࡕࡨࡷࡸ࡯࡯࡯ࠤᏹ"): [bstack11ll1ll_opy_ (u"ࠦࡸࡺࡡࡳࡶࡳࡥࡹ࡮ࠢᏺ"), bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡶࡪࡦ࡯࡬ࡦࡦࠥᏻ"), bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡷࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠢᏼ"), bstack11ll1ll_opy_ (u"ࠢࡪࡶࡨࡱࡸࠨᏽ")],
    bstack11ll1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡥࡲࡲ࡫࡯ࡧ࠯ࡅࡲࡲ࡫࡯ࡧࠣ᏾"): [bstack11ll1ll_opy_ (u"ࠤ࡬ࡲࡻࡵࡣࡢࡶ࡬ࡳࡳࡥࡰࡢࡴࡤࡱࡸࠨ᏿"), bstack11ll1ll_opy_ (u"ࠥࡥࡷ࡭ࡳࠣ᐀")],
    bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡆࡪࡺࡷࡹࡷ࡫ࡄࡦࡨࠥᐁ"): [bstack11ll1ll_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᐂ"), bstack11ll1ll_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢᐃ"), bstack11ll1ll_opy_ (u"ࠢࡧࡷࡱࡧࠧᐄ"), bstack11ll1ll_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᐅ"), bstack11ll1ll_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦᐆ"), bstack11ll1ll_opy_ (u"ࠥ࡭ࡩࡹࠢᐇ")],
    bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲࡫࡯ࡸࡵࡷࡵࡩࡸ࠴ࡓࡶࡤࡕࡩࡶࡻࡥࡴࡶࠥᐈ"): [bstack11ll1ll_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥᐉ"), bstack11ll1ll_opy_ (u"ࠨࡰࡢࡴࡤࡱࠧᐊ"), bstack11ll1ll_opy_ (u"ࠢࡱࡣࡵࡥࡲࡥࡩ࡯ࡦࡨࡼࠧᐋ")],
    bstack11ll1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡴࡸࡲࡳ࡫ࡲ࠯ࡅࡤࡰࡱࡏ࡮ࡧࡱࠥᐌ"): [bstack11ll1ll_opy_ (u"ࠤࡺ࡬ࡪࡴࠢᐍ"), bstack11ll1ll_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࠥᐎ")],
    bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡎࡰࡦࡨࡏࡪࡿࡷࡰࡴࡧࡷࠧᐏ"): [bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᐐ"), bstack11ll1ll_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᐑ")],
    bstack11ll1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡐࡥࡷࡱࠢᐒ"): [bstack11ll1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᐓ"), bstack11ll1ll_opy_ (u"ࠤࡤࡶ࡬ࡹࠢᐔ"), bstack11ll1ll_opy_ (u"ࠥ࡯ࡼࡧࡲࡨࡵࠥᐕ")],
}
_1ll1l1l1l11_opy_ = set()
class bstack1l1l1l1l1l1_opy_(bstack1lllll111l1_opy_):
    bstack1l11l111lll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡩ࡫࡫ࡲࡳࡧࡧࠦᐖ")
    bstack1l111llll1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࡏࡎࡇࡑࠥᐗ")
    bstack1l111lll11l_opy_ = bstack11ll1ll_opy_ (u"ࠨࡅࡓࡔࡒࡖࠧᐘ")
    bstack1l11l1111l1_opy_: Callable
    bstack1l111llllll_opy_: Callable
    def __init__(self, bstack1l1l11l1l11_opy_, bstack1ll1ll11l11_opy_):
        super().__init__()
        self.bstack1l111ll1ll1_opy_ = bstack1ll1ll11l11_opy_
        if os.getenv(bstack11ll1ll_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡏ࠲࠳࡜ࠦᐙ"), bstack11ll1ll_opy_ (u"ࠣ࠳ࠥᐚ")) != bstack11ll1ll_opy_ (u"ࠤ࠴ࠦᐛ") or not self.is_enabled():
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠥࠦᐜ") + str(self.__class__.__name__) + bstack11ll1ll_opy_ (u"ࠦࠥࡪࡩࡴࡣࡥࡰࡪࡪࠢᐝ"))
            return
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1ll111l_opy_)
        for event in bstack1lll1l111l1_opy_:
            for state in bstack1lll1ll1ll1_opy_:
                TestFramework.bstack1lllll1l11l_opy_((event, state), self.bstack1l11l1ll1l1_opy_)
        bstack1l1l11l1l11_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.POST), self.bstack1l11l11l1l1_opy_)
        self.bstack1l11l1111l1_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l11l11l_opy_(bstack1l1l1l1l1l1_opy_.bstack1l111llll1l_opy_, self.bstack1l11l1111l1_opy_)
        self.bstack1l111llllll_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l11l11l_opy_(bstack1l1l1l1l1l1_opy_.bstack1l111lll11l_opy_, self.bstack1l111llllll_opy_)
        self.bstack1l11l11ll1l_opy_ = builtins.print
        builtins.print = self.bstack1l11l111l1l_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1l1lllll111_opy_() and instance:
            bstack1l11l1l1l1l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllllllll1_opy_
            if test_framework_state == bstack1lll1l111l1_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1l111l1_opy_.LOG:
                bstack111111ll11_opy_ = datetime.now()
                entries = f.bstack1ll11l111ll_opy_(instance, bstack1lllllllll1_opy_)
                if entries:
                    self.bstack1ll1111l111_opy_(instance, entries)
                    instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࠧᐞ"), datetime.now() - bstack111111ll11_opy_)
                    f.bstack1ll11lll1ll_opy_(instance, bstack1lllllllll1_opy_)
                instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᐟ"), datetime.now() - bstack1l11l1l1l1l_opy_)
                return # do not send this event with the bstack1l111ll111l_opy_ bstack1l11l11111l_opy_
            elif (
                test_framework_state == bstack1lll1l111l1_opy_.TEST
                and test_hook_state == bstack1lll1ll1ll1_opy_.POST
                and not f.bstack1lllll1llll_opy_(instance, TestFramework.bstack1l1lll1llll_opy_)
            ):
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠢࡥࡴࡲࡴࡵ࡯࡮ࡨࠢࡧࡹࡪࠦࡴࡰࠢ࡯ࡥࡨࡱࠠࡰࡨࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࠧᐠ") + str(TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1l1lll1llll_opy_)) + bstack11ll1ll_opy_ (u"ࠣࠤᐡ"))
                f.bstack1lllllll1l1_opy_(instance, bstack1l1l1l1l1l1_opy_.bstack1l11l111lll_opy_, True)
                return # do not send this event bstack1l11l1ll111_opy_ bstack1l111llll11_opy_
            elif (
                f.get_state(instance, bstack1l1l1l1l1l1_opy_.bstack1l11l111lll_opy_, False)
                and test_framework_state == bstack1lll1l111l1_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1ll1ll1_opy_.POST
                and f.bstack1lllll1llll_opy_(instance, TestFramework.bstack1l1lll1llll_opy_)
            ):
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠤ࡬ࡲ࡯࡫ࡣࡵ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡘࡊ࡙ࡔ࠭ࠢࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡓࡓࡘ࡚ࠠࠣᐢ") + str(TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1l1lll1llll_opy_)) + bstack11ll1ll_opy_ (u"ࠥࠦᐣ"))
                self.bstack1l11l1ll1l1_opy_(f, instance, (bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), *args, **kwargs)
            bstack111111ll11_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1l11ll_opy_ = sorted(
                filter(lambda x: x.get(bstack11ll1ll_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᐤ"), None), data.pop(bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᐥ"), {}).values()),
                key=lambda x: x[bstack11ll1ll_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᐦ")],
            )
            if bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_ in data:
                data.pop(bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_)
            data.update({bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᐧ"): bstack1l11l1l11ll_opy_})
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠣ࡬ࡶࡳࡳࡀࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᐨ"), datetime.now() - bstack111111ll11_opy_)
            bstack111111ll11_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l111ll11ll_opy_)
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᐩ"), datetime.now() - bstack111111ll11_opy_)
            self.bstack1l11l11111l_opy_(instance, bstack1lllllllll1_opy_, event_json=event_json)
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᐪ"), datetime.now() - bstack1l11l1l1l1l_opy_)
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
        bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack111l1l11l_opy_.value)
        self.bstack1l111ll1ll1_opy_.bstack1lll1l111ll_opy_(instance, f, bstack1lllllllll1_opy_, *args, **kwargs)
        bstack1llll11l11l_opy_.end(EVENTS.bstack111l1l11l_opy_.value, bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᐫ"), bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᐬ"), status=True, failure=None, test_name=None)
    def bstack1lll1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l111ll1ll1_opy_.bstack1lll1l1l111_opy_(instance, f, bstack1lllllllll1_opy_, *args, **kwargs)
        self.bstack1l11l1l1lll_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l111lll111_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1l11l1l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡖࡨࡷࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡋࡶࡦࡰࡷࠤ࡬ࡘࡐࡄࠢࡦࡥࡱࡲ࠺ࠡࡐࡲࠤࡻࡧ࡬ࡪࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡩࡧࡴࡢࠤᐭ"))
            return
        bstack111111ll11_opy_ = datetime.now()
        try:
            r = self.bstack1llllll1l1l_opy_.TestSessionEvent(req)
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡨࡺࡪࡴࡴࠣᐮ"), datetime.now() - bstack111111ll11_opy_)
            f.bstack1lllllll1l1_opy_(instance, self.bstack1l111ll1ll1_opy_.bstack1llll11111l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11ll1ll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᐯ") + str(r) + bstack11ll1ll_opy_ (u"ࠤࠥᐰ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᐱ") + str(e) + bstack11ll1ll_opy_ (u"ࠦࠧᐲ"))
            traceback.print_exc()
            raise e
    def bstack1l11l11l1l1_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        _driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        _1l11l11l111_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llll1ll111_opy_.bstack1l1lll11ll1_opy_(method_name):
            return
        if f.bstack1l1ll1lll1l_opy_(*args) == bstack1llll1ll111_opy_.bstack1l11l1l11l1_opy_:
            bstack1l11l1l1l1l_opy_ = datetime.now()
            screenshot = result.get(bstack11ll1ll_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᐳ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤ࡮ࡳࡡࡨࡧࠣࡦࡦࡹࡥ࠷࠶ࠣࡷࡹࡸࠢᐴ"))
                return
            bstack1ll111l1l11_opy_ = self.bstack1l11l11lll1_opy_(instance)
            if bstack1ll111l1l11_opy_:
                entry = bstack1l1llll111l_opy_(TestFramework.bstack1l111ll1l1l_opy_, screenshot)
                self.bstack1ll1111l111_opy_(bstack1ll111l1l11_opy_, [entry])
                instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡦࡺࡨࡧࡺࡺࡥࠣᐵ"), datetime.now() - bstack1l11l1l1l1l_opy_)
            else:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠣࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡵࡧࡶࡸࠥ࡬࡯ࡳࠢࡺ࡬࡮ࡩࡨࠡࡶ࡫࡭ࡸࠦࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠣࡻࡦࡹࠠࡵࡣ࡮ࡩࡳࠦࡢࡺࠢࡧࡶ࡮ࡼࡥࡳ࠿ࠣࡿࢂࠨᐶ").format(instance.ref()))
        event = {}
        bstack1ll111l1l11_opy_ = self.bstack1l11l11lll1_opy_(instance)
        if bstack1ll111l1l11_opy_:
            self.bstack1l11l11llll_opy_(event, bstack1ll111l1l11_opy_)
            if event.get(bstack11ll1ll_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᐷ")):
                self.bstack1ll1111l111_opy_(bstack1ll111l1l11_opy_, event[bstack11ll1ll_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᐸ")])
            else:
                self.logger.debug(bstack11ll1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡰࡴ࡭ࡳࠡࡨࡲࡶࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡨࡺࡪࡴࡴࠣᐹ"))
    @measure(event_name=EVENTS.bstack1l111lllll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1ll1111l111_opy_(
        self,
        bstack1ll111l1l11_opy_: bstack1lll1l1l1ll_opy_,
        entries: List[bstack1l1llll111l_opy_],
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1llll1l11ll_opy_)
        req.execution_context.hash = str(bstack1ll111l1l11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111l1l11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111l1l11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll1ll11ll_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll11ll1ll_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll111l1l11_opy_, TestFramework.bstack1lll11llll1_opy_)
            log_entry.test_framework_state = bstack1ll111l1l11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11ll1ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᐺ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11ll1ll_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᐻ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llllll1l_opy_
                log_entry.file_path = entry.bstack1111lll_opy_
        def bstack1l1lll11lll_opy_():
            bstack111111ll11_opy_ = datetime.now()
            try:
                self.bstack1llllll1l1l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l111ll1l1l_opy_:
                    bstack1ll111l1l11_opy_.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᐼ"), datetime.now() - bstack111111ll11_opy_)
                elif entry.kind == TestFramework.bstack1l11l11ll11_opy_:
                    bstack1ll111l1l11_opy_.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᐽ"), datetime.now() - bstack111111ll11_opy_)
                else:
                    bstack1ll111l1l11_opy_.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡ࡯ࡳ࡬ࠨᐾ"), datetime.now() - bstack111111ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll1ll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᐿ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll111llll_opy_.enqueue(bstack1l1lll11lll_opy_)
    @measure(event_name=EVENTS.bstack1l11l1l1111_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1l11l11111l_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        event_json=None,
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l11ll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11ll1ll_opy_)
        req.test_framework_state = bstack1lllllllll1_opy_[0].name
        req.test_hook_state = bstack1lllllllll1_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l11ll1l_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l111ll11ll_opy_)).encode(bstack11ll1ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᑀ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1l1lll11lll_opy_():
            bstack111111ll11_opy_ = datetime.now()
            try:
                self.bstack1llllll1l1l_opy_.TestFrameworkEvent(req)
                instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡨࡺࡪࡴࡴࠣᑁ"), datetime.now() - bstack111111ll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11ll1ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᑂ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll111llll_opy_.enqueue(bstack1l1lll11lll_opy_)
    def bstack1l11l11lll1_opy_(self, instance: bstack1llll111l1l_opy_):
        bstack1l11l111ll1_opy_ = TestFramework.bstack1l11l11l1ll_opy_(instance.context)
        for t in bstack1l11l111ll1_opy_:
            bstack1lll1111111_opy_ = TestFramework.get_state(t, bstack1lll11111l1_opy_.bstack1lll1l1llll_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111111_opy_):
                return t
    def bstack1l111lll1ll_opy_(self, message):
        self.bstack1l11l1111l1_opy_(message + bstack11ll1ll_opy_ (u"ࠢ࡝ࡰࠥᑃ"))
    def log_error(self, message):
        self.bstack1l111llllll_opy_(message + bstack11ll1ll_opy_ (u"ࠣ࡞ࡱࠦᑄ"))
    def bstack1l11l11l11l_opy_(self, level, original_func):
        def bstack1l11l111111_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11ll1ll_opy_ (u"ࠤࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࠥᑅ") in message or bstack11ll1ll_opy_ (u"ࠥ࡟ࡘࡊࡋࡄࡎࡌࡡࠧᑆ") in message or bstack11ll1ll_opy_ (u"ࠦࡠ࡝ࡥࡣࡆࡵ࡭ࡻ࡫ࡲࡎࡱࡧࡹࡱ࡫࡝ࠣᑇ") in message:
                return return_value
            bstack1l11l111ll1_opy_ = TestFramework.bstack1l11l1ll11l_opy_()
            if not bstack1l11l111ll1_opy_:
                return return_value
            bstack1ll111l1l11_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l111ll1_opy_
                    if TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1lll11llll1_opy_)
                ),
                None,
            )
            if not bstack1ll111l1l11_opy_:
                return return_value
            entry = bstack1l1llll111l_opy_(TestFramework.bstack1ll11111lll_opy_, message, level)
            self.bstack1ll1111l111_opy_(bstack1ll111l1l11_opy_, [entry])
            return return_value
        return bstack1l11l111111_opy_
    def bstack1l11l111l1l_opy_(self):
        def bstack1l11l1l1l11_opy_(*args, **kwargs):
            try:
                self.bstack1l11l11ll1l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11ll1ll_opy_ (u"ࠬࠦࠧᑈ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11ll1ll_opy_ (u"ࠨࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫ࠢᑉ") in message:
                    return
                bstack1l11l111ll1_opy_ = TestFramework.bstack1l11l1ll11l_opy_()
                if not bstack1l11l111ll1_opy_:
                    return
                bstack1ll111l1l11_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l111ll1_opy_
                        if TestFramework.bstack1lllll1llll_opy_(instance, TestFramework.bstack1lll11llll1_opy_)
                    ),
                    None,
                )
                if not bstack1ll111l1l11_opy_:
                    return
                entry = bstack1l1llll111l_opy_(TestFramework.bstack1ll11111lll_opy_, message, bstack1l1l1l1l1l1_opy_.bstack1l111llll1l_opy_)
                self.bstack1ll1111l111_opy_(bstack1ll111l1l11_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l11ll1l_opy_(bstack1lll1ll1l11_opy_ (u"ࠢ࡜ࡇࡹࡩࡳࡺࡄࡪࡵࡳࡥࡹࡩࡨࡦࡴࡐࡳࡩࡻ࡬ࡦ࡟ࠣࡐࡴ࡭ࠠࡤࡣࡳࡸࡺࡸࡥࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࡨࢁࠧᑊ"))
                except:
                    pass
        return bstack1l11l1l1l11_opy_
    def bstack1l11l11llll_opy_(self, event: dict, instance=None) -> None:
        global _1ll1l1l1l11_opy_
        levels = [bstack11ll1ll_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᑋ"), bstack11ll1ll_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᑌ")]
        bstack1l11l1111ll_opy_ = bstack11ll1ll_opy_ (u"ࠥࠦᑍ")
        if instance is not None:
            try:
                bstack1l11l1111ll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll11llll1_opy_)
            except Exception as e:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡻࡩࡥࠢࡩࡶࡴࡳࠠࡪࡰࡶࡸࡦࡴࡣࡦࠤᑎ").format(e))
        bstack1l11l1lll11_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᑏ")]
                bstack1ll1111llll_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1l1lll1l1l1_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1111llll_opy_):
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡱࡳࡹࠦࡰࡳࡧࡶࡩࡳࡺࠠࡧࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡖࡨࡷࡹࠦࡡ࡯ࡦࠣࡆࡺ࡯࡬ࡥࠢ࡯ࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᑐ").format(bstack1ll1111llll_opy_))
                    continue
                file_names = os.listdir(bstack1ll1111llll_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1111llll_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1l1l1l11_opy_:
                        self.logger.info(bstack11ll1ll_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧᑑ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1l1ll1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1l1ll1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11ll1ll_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᑒ"):
                                entry = bstack1l1llll111l_opy_(
                                    kind=bstack11ll1ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᑓ"),
                                    message=bstack11ll1ll_opy_ (u"ࠥࠦᑔ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1llllll1l_opy_=file_size,
                                    bstack1ll111l11l1_opy_=bstack11ll1ll_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᑕ"),
                                    bstack1111lll_opy_=os.path.abspath(file_path),
                                    bstack111lll111_opy_=bstack1l11l1111ll_opy_
                                )
                            elif level == bstack11ll1ll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᑖ"):
                                entry = bstack1l1llll111l_opy_(
                                    kind=bstack11ll1ll_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᑗ"),
                                    message=bstack11ll1ll_opy_ (u"ࠢࠣᑘ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1llllll1l_opy_=file_size,
                                    bstack1ll111l11l1_opy_=bstack11ll1ll_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᑙ"),
                                    bstack1111lll_opy_=os.path.abspath(file_path),
                                    bstack1ll1l11ll11_opy_=bstack1l11l1111ll_opy_
                                )
                            bstack1l11l1lll11_opy_.append(entry)
                            _1ll1l1l1l11_opy_.add(abs_path)
                        except Exception as bstack1l11l1lll1l_opy_:
                            self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡸࡡࡪࡵࡨࡨࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣᑚ").format(bstack1l11l1lll1l_opy_))
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡲࡢ࡫ࡶࡩࡩࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᑛ").format(e))
        event[bstack11ll1ll_opy_ (u"ࠦࡱࡵࡧࡴࠤᑜ")] = bstack1l11l1lll11_opy_
class bstack1l111ll11ll_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1l111l_opy_ = set()
        kwargs[bstack11ll1ll_opy_ (u"ࠧࡹ࡫ࡪࡲ࡮ࡩࡾࡹࠢᑝ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l111ll11l1_opy_(obj, self.bstack1l11l1l111l_opy_)
def bstack1l111ll1l11_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l111ll11l1_opy_(obj, bstack1l11l1l111l_opy_=None, max_depth=3):
    if bstack1l11l1l111l_opy_ is None:
        bstack1l11l1l111l_opy_ = set()
    if id(obj) in bstack1l11l1l111l_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1l111l_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l111l11_opy_ = TestFramework.bstack1ll1l11lll1_opy_(obj)
    bstack1l111ll1lll_opy_ = next((k.lower() in bstack1l11l111l11_opy_.lower() for k in bstack1l111lll1l1_opy_.keys()), None)
    if bstack1l111ll1lll_opy_:
        obj = TestFramework.bstack1l1llll1lll_opy_(obj, bstack1l111lll1l1_opy_[bstack1l111ll1lll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11ll1ll_opy_ (u"ࠨ࡟ࡠࡵ࡯ࡳࡹࡹ࡟ࡠࠤᑞ")):
            keys = getattr(obj, bstack11ll1ll_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥᑟ"), [])
        elif hasattr(obj, bstack11ll1ll_opy_ (u"ࠣࡡࡢࡨ࡮ࡩࡴࡠࡡࠥᑠ")):
            keys = getattr(obj, bstack11ll1ll_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦᑡ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11ll1ll_opy_ (u"ࠥࡣࠧᑢ"))}
        if not obj and bstack1l11l111l11_opy_ == bstack11ll1ll_opy_ (u"ࠦࡵࡧࡴࡩ࡮࡬ࡦ࠳ࡖ࡯ࡴ࡫ࡻࡔࡦࡺࡨࠣᑣ"):
            obj = {bstack11ll1ll_opy_ (u"ࠧࡶࡡࡵࡪࠥᑤ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l111ll1l11_opy_(key) or str(key).startswith(bstack11ll1ll_opy_ (u"ࠨ࡟ࠣᑥ")):
            continue
        if value is not None and bstack1l111ll1l11_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l111ll11l1_opy_(value, bstack1l11l1l111l_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l111ll11l1_opy_(o, bstack1l11l1l111l_opy_, max_depth) for o in value]))
    return result or None