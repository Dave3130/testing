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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
    bstack1llll111l1l_opy_,
    bstack1lll1lll1ll_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11lll11_opy_, bstack1llllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_, bstack1lll1l1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l11l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1l11111_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11111111l_opy_ import bstack11ll1111l1_opy_, bstack11l1l111ll_opy_, bstack1lll111ll1_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll11l11ll_opy_(bstack1lll1l11111_opy_):
    bstack1lll11l1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡵ࡭ࡻ࡫ࡲࡴࠤᄶ")
    bstack1lll1l1llll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᄷ")
    bstack1lll1l11lll_opy_ = bstack11ll1ll_opy_ (u"ࠧࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᄸ")
    bstack1lll1l11l11_opy_ = bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᄹ")
    bstack1lll1ll1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡥࡲࡦࡨࡶࠦᄺ")
    bstack1llll11111l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡣࡳࡧࡤࡸࡪࡪࠢᄻ")
    bstack1lll11lllll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᄼ")
    bstack1lll1lllll1_opy_ = bstack11ll1ll_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡵࡷࡥࡹࡻࡳࠣᄽ")
    def __init__(self):
        super().__init__(bstack1lll1l1l1l1_opy_=self.bstack1lll11l1l1l_opy_, frameworks=[bstack1llll1ll111_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.BEFORE_EACH, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1l11l1l_opy_)
        if bstack1llllll1l1_opy_():
            TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1l1lll1_opy_)
        else:
            TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1ll111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l11l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1l1ll11_opy_ = self.bstack1lll1llllll_opy_(instance.context)
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡲࡤ࡫ࡪࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᄾ") + str(bstack1lllllllll1_opy_) + bstack11ll1ll_opy_ (u"ࠧࠨᄿ"))
            return
        f.bstack1lllllll1l1_opy_(instance, bstack1lll11l11ll_opy_.bstack1lll1l1llll_opy_, bstack1lll1l1ll11_opy_)
    def bstack1lll1llllll_opy_(self, context: bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_= True):
        if bstack1lll1lll11l_opy_:
            bstack1lll1l1ll11_opy_ = self.bstack1lll1l11ll1_opy_(context, reverse=True)
        else:
            bstack1lll1l1ll11_opy_ = self.bstack1lll11ll11l_opy_(context, reverse=True)
        return [f for f in bstack1lll1l1ll11_opy_ if f[1].state != bstack1llll1l1ll1_opy_.QUIT]
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11l1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not bstack1lll11lll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅀ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠢࠣᅁ"))
            return
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll11l11ll_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅂ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠤࠥᅃ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᅄ"))
        bstack1lll1llll1l_opy_, bstack1llll111l11_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1llll1l_opy_()
        if not page:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅅ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠧࠨᅆ"))
            return
        bstack1111l1l1ll_opy_ = getattr(args[0], bstack11ll1ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᅇ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧᅈ")).get(bstack11ll1ll_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᅉ")):
            try:
                page.evaluate(bstack11ll1ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᅊ"),
                            bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧᅋ") + json.dumps(
                                bstack1111l1l1ll_opy_) + bstack11ll1ll_opy_ (u"ࠦࢂࢃࠢᅌ"))
            except Exception as e:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥᅍ"), e)
    def bstack1lll1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11l1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not bstack1lll11lll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅎ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠢࠣᅏ"))
            return
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll11l11ll_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅐ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠤࠥᅑ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᅒ"))
        bstack1lll1llll1l_opy_, bstack1llll111l11_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1llll1l_opy_()
        if not page:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅓ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠧࠨᅔ"))
            return
        status = f.get_state(instance, TestFramework.bstack1llll1111l1_opy_, None)
        if not status:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅕ") + str(bstack1lllllllll1_opy_) + bstack11ll1ll_opy_ (u"ࠢࠣᅖ"))
            return
        bstack1lll11ll111_opy_ = {bstack11ll1ll_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᅗ"): status.lower()}
        bstack1lll11l1lll_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1111l_opy_, None)
        if status.lower() == bstack11ll1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᅘ") and bstack1lll11l1lll_opy_ is not None:
            bstack1lll11ll111_opy_[bstack11ll1ll_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᅙ")] = bstack1lll11l1lll_opy_[0][bstack11ll1ll_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᅚ")][0] if isinstance(bstack1lll11l1lll_opy_, list) else str(bstack1lll11l1lll_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᅛ")).get(bstack11ll1ll_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᅜ")):
            try:
                page.evaluate(
                        bstack11ll1ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᅝ"),
                        bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥ࠭ᅞ")
                        + json.dumps(bstack1lll11ll111_opy_)
                        + bstack11ll1ll_opy_ (u"ࠤࢀࠦᅟ")
                    )
            except Exception as e:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡼࡿࠥᅠ"), e)
    def bstack1lll1l111ll_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11l1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not bstack1lll11lll11_opy_:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠦࡲࡧࡲ࡬ࡡࡲ࠵࠶ࡿ࡟ࡴࡻࡱࡧ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᅡ"))
            return
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll11l11ll_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅢ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠨࠢᅣ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᅤ"))
        bstack1lll1llll1l_opy_, bstack1llll111l11_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1llll1l_opy_()
        if not page:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣ࡯ࡤࡶࡰࡥ࡯࠲࠳ࡼࡣࡸࡿ࡮ࡤ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅥ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠤࠥᅦ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11ll1ll_opy_ (u"ࠥࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡖࡽࡳࡩ࠺ࠣᅧ") + str(timestamp)
        try:
            page.evaluate(
                bstack11ll1ll_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᅨ"),
                bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᅩ").format(
                    json.dumps(
                        {
                            bstack11ll1ll_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᅪ"): bstack11ll1ll_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤᅫ"),
                            bstack11ll1ll_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅬ"): {
                                bstack11ll1ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᅭ"): bstack11ll1ll_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢᅮ"),
                                bstack11ll1ll_opy_ (u"ࠦࡩࡧࡴࡢࠤᅯ"): data,
                                bstack11ll1ll_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦᅰ"): bstack11ll1ll_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧᅱ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡳ࠶࠷ࡹࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡻࡾࠤᅲ"), e)
    def bstack1lll1l1l111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11l1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll11l11ll_opy_.bstack1llll11111l_opy_, False):
            return
        self.bstack1llllll1ll1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l11ll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11ll1ll_opy_)
        req.test_framework_state = bstack1lllllllll1_opy_[0].name
        req.test_hook_state = bstack1lllllllll1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11llll1_opy_)
        for bstack1lll1llll11_opy_ in bstack1lll11l1l11_opy_.bstack1llll111111_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11ll1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢᅳ")
                if bstack1lll11lll11_opy_
                else bstack11ll1ll_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣᅴ")
            )
            session.ref = bstack1lll1llll11_opy_.ref()
            session.hub_url = bstack1lll11l1l11_opy_.get_state(bstack1lll1llll11_opy_, bstack1lll11l1l11_opy_.bstack1lll11lll1l_opy_, bstack11ll1ll_opy_ (u"ࠥࠦᅵ"))
            session.framework_name = bstack1lll1llll11_opy_.framework_name
            session.framework_version = bstack1lll1llll11_opy_.framework_version
            session.framework_session_id = bstack1lll11l1l11_opy_.get_state(bstack1lll1llll11_opy_, bstack1lll11l1l11_opy_.bstack1lll11l1ll1_opy_, bstack11ll1ll_opy_ (u"ࠦࠧᅶ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll11l11ll_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅷ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠨࠢᅸ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅹ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠣࠤᅺ"))
        bstack1lll1llll1l_opy_, bstack1llll111l11_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1llll1l_opy_()
        if not page:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅻ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠥࠦᅼ"))
            return
        return page
    def bstack1lll1lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll11l11l1_opy_ = {}
        for bstack1lll1llll11_opy_ in bstack1lll11l1l11_opy_.bstack1llll111111_opy_.values():
            caps = bstack1lll11l1l11_opy_.get_state(bstack1lll1llll11_opy_, bstack1lll11l1l11_opy_.bstack1lll11ll1l1_opy_, bstack11ll1ll_opy_ (u"ࠦࠧᅽ"))
        bstack1lll11l11l1_opy_[bstack11ll1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥᅾ")] = caps.get(bstack11ll1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢᅿ"), bstack11ll1ll_opy_ (u"ࠢࠣᆀ"))
        bstack1lll11l11l1_opy_[bstack11ll1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢᆁ")] = caps.get(bstack11ll1ll_opy_ (u"ࠤࡲࡷࠧᆂ"), bstack11ll1ll_opy_ (u"ࠥࠦᆃ"))
        bstack1lll11l11l1_opy_[bstack11ll1ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᆄ")] = caps.get(bstack11ll1ll_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᆅ"), bstack11ll1ll_opy_ (u"ࠨࠢᆆ"))
        bstack1lll11l11l1_opy_[bstack11ll1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣᆇ")] = caps.get(bstack11ll1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥᆈ"), bstack11ll1ll_opy_ (u"ࠤࠥᆉ"))
        return bstack1lll11l11l1_opy_
    def bstack1lll1lll1l1_opy_(self, page: object, bstack1lll1ll1111_opy_, args={}):
        try:
            bstack1llll1111ll_opy_ = bstack11ll1ll_opy_ (u"ࠥࠦࠧ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࠪ࠱࠲࠳ࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠮ࠦࡻࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡳ࡫ࡷࠡࡒࡵࡳࡲ࡯ࡳࡦࠪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠰ࠥࡸࡥ࡫ࡧࡦࡸ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠲ࡵࡻࡳࡩࠪࡵࡩࡸࡵ࡬ࡷࡧࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢀ࡬࡮ࡠࡤࡲࡨࡾࢃࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࢁ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࡽࠪࠪࡾࡥࡷ࡭࡟࡫ࡵࡲࡲࢂ࠯ࠢࠣࠤᆊ")
            bstack1lll1ll1111_opy_ = bstack1lll1ll1111_opy_.replace(bstack11ll1ll_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆋ"), bstack11ll1ll_opy_ (u"ࠧࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷࠧᆌ"))
            script = bstack1llll1111ll_opy_.format(fn_body=bstack1lll1ll1111_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡅࡳࡴࡲࡶࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶ࠯ࠤࠧᆍ") + str(e) + bstack11ll1ll_opy_ (u"ࠢࠣᆎ"))