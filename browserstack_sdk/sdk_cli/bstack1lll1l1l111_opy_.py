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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import (
    bstack1llll11llll_opy_,
    bstack1llll11l1l1_opy_,
    bstack1llll1l1l11_opy_,
    bstack1lll1l1l1ll_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11ll1ll_opy_, bstack1111ll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llll11ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_, bstack1lll1l11lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll11l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll1111l1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11ll111ll_opy_ import bstack1l1ll1llll_opy_, bstack1l11ll11l1_opy_, bstack1l1111l11_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1llllll_opy_(bstack1llll1111l1_opy_):
    bstack1lll1llll11_opy_ = bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡷ࡯ࡶࡦࡴࡶࠦᄱ")
    bstack1lll11lllll_opy_ = bstack11ll1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄲ")
    bstack1lll1ll111l_opy_ = bstack11ll1l_opy_ (u"ࠢ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᄳ")
    bstack1lll1ll11ll_opy_ = bstack11ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᄴ")
    bstack1lll1l111l1_opy_ = bstack11ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡠࡴࡨࡪࡸࠨᄵ")
    bstack1lll1ll1l11_opy_ = bstack11ll1l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡥࡵࡩࡦࡺࡥࡥࠤᄶ")
    bstack1lll1lll11l_opy_ = bstack11ll1l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢᄷ")
    bstack1lll1l1llll_opy_ = bstack11ll1l_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡷࡹࡧࡴࡶࡵࠥᄸ")
    def __init__(self):
        super().__init__(bstack1lll11lll11_opy_=self.bstack1lll1llll11_opy_, frameworks=[bstack1llll11ll11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.BEFORE_EACH, bstack1lll11lll1l_opy_.POST), self.bstack1lll1ll1lll_opy_)
        if bstack1111ll1ll_opy_():
            TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1llll1l_opy_)
        else:
            TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1lll1llll1l_opy_)
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1l11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1l1ll11_opy_ = self.bstack1lll1lll1l1_opy_(instance.context)
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡴࡦ࡭ࡥ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᄹ") + str(bstack1lllllllll1_opy_) + bstack11ll1l_opy_ (u"ࠢࠣᄺ"))
            return
        f.bstack1llll1l1lll_opy_(instance, bstack1lll1llllll_opy_.bstack1lll11lllll_opy_, bstack1lll1l1ll11_opy_)
    def bstack1lll1lll1l1_opy_(self, context: bstack1lll1l1l1ll_opy_, bstack1lll11ll11l_opy_= True):
        if bstack1lll11ll11l_opy_:
            bstack1lll1l1ll11_opy_ = self.bstack1llll1111ll_opy_(context, reverse=True)
        else:
            bstack1lll1l1ll11_opy_ = self.bstack1lll1l11l1l_opy_(context, reverse=True)
        return [f for f in bstack1lll1l1ll11_opy_ if f[1].state != bstack1llll11llll_opy_.QUIT]
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1lll_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄻ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠤࠥᄼ"))
            return
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll1llllll_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄽ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧᄾ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᄿ"))
        bstack1lll1lll1ll_opy_, bstack1llll11111l_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1lll1ll_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅀ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣᅁ"))
            return
        bstack11l111llll_opy_ = getattr(args[0], bstack11ll1l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᅂ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠢᅃ")).get(bstack11ll1l_opy_ (u"ࠥࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᅄ")):
            try:
                page.evaluate(bstack11ll1l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᅅ"),
                            bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩᅆ") + json.dumps(
                                bstack11l111llll_opy_) + bstack11ll1l_opy_ (u"ࠨࡽࡾࠤᅇ"))
            except Exception as e:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧᅈ"), e)
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1lll_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅉ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠤࠥᅊ"))
            return
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll1llllll_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅋ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧᅌ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᅍ"))
        bstack1lll1lll1ll_opy_, bstack1llll11111l_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1lll1ll_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᅎ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠢࠣᅏ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1l11111_opy_, None)
        if not status:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᅐ") + str(bstack1lllllllll1_opy_) + bstack11ll1l_opy_ (u"ࠤࠥᅑ"))
            return
        bstack1lll1ll1ll1_opy_ = {bstack11ll1l_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᅒ"): status.lower()}
        bstack1lll1ll1111_opy_ = f.get_state(instance, TestFramework.bstack1lll1l11l11_opy_, None)
        if status.lower() == bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᅓ") and bstack1lll1ll1111_opy_ is not None:
            bstack1lll1ll1ll1_opy_[bstack11ll1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᅔ")] = bstack1lll1ll1111_opy_[0][bstack11ll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᅕ")][0] if isinstance(bstack1lll1ll1111_opy_, list) else str(bstack1lll1ll1111_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧᅖ")).get(bstack11ll1l_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧᅗ")):
            try:
                page.evaluate(
                        bstack11ll1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᅘ"),
                        bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࠨᅙ")
                        + json.dumps(bstack1lll1ll1ll1_opy_)
                        + bstack11ll1l_opy_ (u"ࠦࢂࠨᅚ")
                    )
            except Exception as e:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡾࢁࠧᅛ"), e)
    def bstack1lll1l111ll_opy_(
        self,
        instance: bstack1lll1l11lll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1lll_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠨ࡭ࡢࡴ࡮ࡣࡴ࠷࠱ࡺࡡࡶࡽࡳࡩ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᅜ"))
            return
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll1llllll_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅝ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠣࠤᅞ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᅟ"))
        bstack1lll1lll1ll_opy_, bstack1llll11111l_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1lll1ll_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡱࡦࡸ࡫ࡠࡱ࠴࠵ࡾࡥࡳࡺࡰࡦ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅠ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧᅡ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11ll1l_opy_ (u"ࠧࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡘࡿ࡮ࡤ࠼ࠥᅢ") + str(timestamp)
        try:
            page.evaluate(
                bstack11ll1l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᅣ"),
                bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬᅤ").format(
                    json.dumps(
                        {
                            bstack11ll1l_opy_ (u"ࠣࡣࡦࡸ࡮ࡵ࡮ࠣᅥ"): bstack11ll1l_opy_ (u"ࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦᅦ"),
                            bstack11ll1l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᅧ"): {
                                bstack11ll1l_opy_ (u"ࠦࡹࡿࡰࡦࠤᅨ"): bstack11ll1l_opy_ (u"ࠧࡇ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠤᅩ"),
                                bstack11ll1l_opy_ (u"ࠨࡤࡢࡶࡤࠦᅪ"): data,
                                bstack11ll1l_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࠨᅫ"): bstack11ll1l_opy_ (u"ࠣࡦࡨࡦࡺ࡭ࠢᅬ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡵ࠱࠲ࡻࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡽࢀࠦᅭ"), e)
    def bstack1llll111111_opy_(
        self,
        instance: bstack1lll1l11lll_opy_,
        f: TestFramework,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1lll_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1llllll_opy_.bstack1lll1ll1l11_opy_, False):
            return
        self.bstack1llll1l11l1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1llll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1lll1_opy_)
        req.test_framework_state = bstack1lllllllll1_opy_[0].name
        req.test_hook_state = bstack1lllllllll1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        for bstack1lll1l1l1l1_opy_ in bstack1lll11l1ll1_opy_.bstack1lll1l1ll1l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠤᅮ")
                if bstack1lll11ll1ll_opy_
                else bstack11ll1l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠥᅯ")
            )
            session.ref = bstack1lll1l1l1l1_opy_.ref()
            session.hub_url = bstack1lll11l1ll1_opy_.get_state(bstack1lll1l1l1l1_opy_, bstack1lll11l1ll1_opy_.bstack1lll11l1lll_opy_, bstack11ll1l_opy_ (u"ࠧࠨᅰ"))
            session.framework_name = bstack1lll1l1l1l1_opy_.framework_name
            session.framework_version = bstack1lll1l1l1l1_opy_.framework_version
            session.framework_session_id = bstack1lll11l1ll1_opy_.get_state(bstack1lll1l1l1l1_opy_, bstack1lll11l1ll1_opy_.bstack1lll1ll1l1l_opy_, bstack11ll1l_opy_ (u"ࠨࠢᅱ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1l1ll11_opy_ = f.get_state(instance, bstack1lll1llllll_opy_.bstack1lll11lllll_opy_, [])
        if not bstack1lll1l1ll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅲ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠣࠤᅳ"))
            return
        if len(bstack1lll1l1ll11_opy_) > 1:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅴ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠥࠦᅵ"))
        bstack1lll1lll1ll_opy_, bstack1llll11111l_opy_ = bstack1lll1l1ll11_opy_[0]
        page = bstack1lll1lll1ll_opy_()
        if not page:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅶ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠧࠨᅷ"))
            return
        return page
    def bstack1lll11l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll11llll1_opy_ = {}
        for bstack1lll1l1l1l1_opy_ in bstack1lll11l1ll1_opy_.bstack1lll1l1ll1l_opy_.values():
            caps = bstack1lll11l1ll1_opy_.get_state(bstack1lll1l1l1l1_opy_, bstack1lll11l1ll1_opy_.bstack1lll1l1111l_opy_, bstack11ll1l_opy_ (u"ࠨࠢᅸ"))
        bstack1lll11llll1_opy_[bstack11ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧᅹ")] = caps.get(bstack11ll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤᅺ"), bstack11ll1l_opy_ (u"ࠤࠥᅻ"))
        bstack1lll11llll1_opy_[bstack11ll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤᅼ")] = caps.get(bstack11ll1l_opy_ (u"ࠦࡴࡹࠢᅽ"), bstack11ll1l_opy_ (u"ࠧࠨᅾ"))
        bstack1lll11llll1_opy_[bstack11ll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᅿ")] = caps.get(bstack11ll1l_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦᆀ"), bstack11ll1l_opy_ (u"ࠣࠤᆁ"))
        bstack1lll11llll1_opy_[bstack11ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥᆂ")] = caps.get(bstack11ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᆃ"), bstack11ll1l_opy_ (u"ࠦࠧᆄ"))
        return bstack1lll11llll1_opy_
    def bstack1lll11l1l11_opy_(self, page: object, bstack1lll11l1l1l_opy_, args={}):
        try:
            bstack1lll11ll111_opy_ = bstack11ll1l_opy_ (u"ࠧࠨࠢࠩࡨࡸࡲࡨࡺࡩࡰࡰࠣࠬ࠳࠴࠮ࡣࡵࡷࡥࡨࡱࡓࡥ࡭ࡄࡶ࡬ࡹࠩࠡࡽࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡶࡸࡶࡳࠦ࡮ࡦࡹࠣࡔࡷࡵ࡭ࡪࡵࡨࠬ࠭ࡸࡥࡴࡱ࡯ࡺࡪ࠲ࠠࡳࡧ࡭ࡩࡨࡺࠩࠡ࠿ࡁࠤࢀࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸ࠴ࡰࡶࡵ࡫ࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡻࡧࡰࡢࡦࡴࡪࡹࡾࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࢃࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࡿࠬࠬࢀࡧࡲࡨࡡ࡭ࡷࡴࡴࡽࠪࠤࠥࠦᆅ")
            bstack1lll11l1l1l_opy_ = bstack1lll11l1l1l_opy_.replace(bstack11ll1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᆆ"), bstack11ll1l_opy_ (u"ࠢࡣࡵࡷࡥࡨࡱࡓࡥ࡭ࡄࡶ࡬ࡹࠢᆇ"))
            script = bstack1lll11ll111_opy_.format(fn_body=bstack1lll11l1l1l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠣࡣ࠴࠵ࡾࡥࡳࡤࡴ࡬ࡴࡹࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡇࡵࡶࡴࡸࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸ࠱ࠦࠢᆈ") + str(e) + bstack11ll1l_opy_ (u"ࠤࠥᆉ"))