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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll111l1_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack1lllll11ll1_opy_,
    bstack1llll1ll11l_opy_,
    bstack1llll1111l1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1lllll1_opy_, bstack1ll111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_, bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1llllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1ll1_opy_ import bstack1lll1ll1l1l_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11ll1l111l_opy_ import bstack1l11ll11l_opy_, bstack1llll1l111_opy_, bstack11l1ll11l_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1llll1l_opy_(bstack1lll1ll1l1l_opy_):
    bstack1lll1ll1lll_opy_ = bstack11l1111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᄵ")
    bstack1llll111111_opy_ = bstack11l1111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᄶ")
    bstack1lll1lll11l_opy_ = bstack11l1111_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᄷ")
    bstack1llll11111l_opy_ = bstack11l1111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄸ")
    bstack1lll1l11l11_opy_ = bstack11l1111_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᄹ")
    bstack1lll11ll1l1_opy_ = bstack11l1111_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᄺ")
    bstack1lll1l1ll1l_opy_ = bstack11l1111_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᄻ")
    bstack1lll1ll1l11_opy_ = bstack11l1111_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᄼ")
    def __init__(self):
        super().__init__(bstack1lll1l1ll11_opy_=self.bstack1lll1ll1lll_opy_, frameworks=[bstack1lllll11111_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.BEFORE_EACH, bstack1lll11l11ll_opy_.POST), self.bstack1lll1l1lll1_opy_)
        if bstack1ll111ll1_opy_():
            TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.POST), self.bstack1lll1l1l11l_opy_)
        else:
            TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.PRE), self.bstack1lll1l1l11l_opy_)
        TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.POST), self.bstack1lll1l1l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11l11l1_opy_ = self.bstack1llll111l11_opy_(instance.context)
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡱࡣࡪࡩ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᄽ") + str(bstack1llllll1lll_opy_) + bstack11l1111_opy_ (u"ࠦࠧᄾ"))
            return
        f.bstack1llllll1111_opy_(instance, bstack1lll1llll1l_opy_.bstack1llll111111_opy_, bstack1lll11l11l1_opy_)
    def bstack1llll111l11_opy_(self, context: bstack1llll1111l1_opy_, bstack1lll1llll11_opy_= True):
        if bstack1lll1llll11_opy_:
            bstack1lll11l11l1_opy_ = self.bstack1lll1lll1l1_opy_(context, reverse=True)
        else:
            bstack1lll11l11l1_opy_ = self.bstack1lll1l111l1_opy_(context, reverse=True)
        return [f for f in bstack1lll11l11l1_opy_ if f[1].state != bstack1lllllll1ll_opy_.QUIT]
    def bstack1lll1l1l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1lll1_opy_(f, instance, bstack1llllll1lll_opy_, *args, **kwargs)
        if not bstack1lll1lllll1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄿ") + str(kwargs) + bstack11l1111_opy_ (u"ࠨࠢᅀ"))
            return
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll1llll1l_opy_.bstack1llll111111_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅁ") + str(kwargs) + bstack11l1111_opy_ (u"ࠣࠤᅂ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᅃ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll111l_opy_ = bstack1lll11l11l1_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11l1111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅄ") + str(kwargs) + bstack11l1111_opy_ (u"ࠦࠧᅅ"))
            return
        bstack11lll11l1l_opy_ = getattr(args[0], bstack11l1111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᅆ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1111_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᅇ")).get(bstack11l1111_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᅈ")):
            try:
                page.evaluate(bstack11l1111_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᅉ"),
                            bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᅊ") + json.dumps(
                                bstack11lll11l1l_opy_) + bstack11l1111_opy_ (u"ࠥࢁࢂࠨᅋ"))
            except Exception as e:
                self.logger.debug(bstack11l1111_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᅌ"), e)
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1lll1_opy_(f, instance, bstack1llllll1lll_opy_, *args, **kwargs)
        if not bstack1lll1lllll1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅍ") + str(kwargs) + bstack11l1111_opy_ (u"ࠨࠢᅎ"))
            return
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll1llll1l_opy_.bstack1llll111111_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅏ") + str(kwargs) + bstack11l1111_opy_ (u"ࠣࠤᅐ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᅑ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll111l_opy_ = bstack1lll11l11l1_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11l1111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅒ") + str(kwargs) + bstack11l1111_opy_ (u"ࠦࠧᅓ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1lll111_opy_, None)
        if not status:
            self.logger.debug(bstack11l1111_opy_ (u"ࠧࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᅔ") + str(bstack1llllll1lll_opy_) + bstack11l1111_opy_ (u"ࠨࠢᅕ"))
            return
        bstack1lll11l1l11_opy_ = {bstack11l1111_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᅖ"): status.lower()}
        bstack1lll1l11ll1_opy_ = f.get_state(instance, TestFramework.bstack1lll11l1l1l_opy_, None)
        if status.lower() == bstack11l1111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᅗ") and bstack1lll1l11ll1_opy_ is not None:
            bstack1lll11l1l11_opy_[bstack11l1111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᅘ")] = bstack1lll1l11ll1_opy_[0][bstack11l1111_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᅙ")][0] if isinstance(bstack1lll1l11ll1_opy_, list) else str(bstack1lll1l11ll1_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1111_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᅚ")).get(bstack11l1111_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᅛ")):
            try:
                page.evaluate(
                        bstack11l1111_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᅜ"),
                        bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࠬᅝ")
                        + json.dumps(bstack1lll11l1l11_opy_)
                        + bstack11l1111_opy_ (u"ࠣࡿࠥᅞ")
                    )
            except Exception as e:
                self.logger.debug(bstack11l1111_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡻࡾࠤᅟ"), e)
    def bstack1lll11lllll_opy_(
        self,
        instance: bstack1lll1ll11ll_opy_,
        f: TestFramework,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1lll1_opy_(f, instance, bstack1llllll1lll_opy_, *args, **kwargs)
        if not bstack1lll1lllll1_opy_:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠥࡱࡦࡸ࡫ࡠࡱ࠴࠵ࡾࡥࡳࡺࡰࡦ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᅠ"))
            return
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll1llll1l_opy_.bstack1llll111111_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅡ") + str(kwargs) + bstack11l1111_opy_ (u"ࠧࠨᅢ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᅣ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll111l_opy_ = bstack1lll11l11l1_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11l1111_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅤ") + str(kwargs) + bstack11l1111_opy_ (u"ࠣࠤᅥ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11l1111_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᅦ") + str(timestamp)
        try:
            page.evaluate(
                bstack11l1111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᅧ"),
                bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᅨ").format(
                    json.dumps(
                        {
                            bstack11l1111_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅩ"): bstack11l1111_opy_ (u"ࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣᅪ"),
                            bstack11l1111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅫ"): {
                                bstack11l1111_opy_ (u"ࠣࡶࡼࡴࡪࠨᅬ"): bstack11l1111_opy_ (u"ࠤࡄࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠨᅭ"),
                                bstack11l1111_opy_ (u"ࠥࡨࡦࡺࡡࠣᅮ"): data,
                                bstack11l1111_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࠥᅯ"): bstack11l1111_opy_ (u"ࠧࡪࡥࡣࡷࡪࠦᅰ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11l1111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡲ࠵࠶ࡿࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࢁࡽࠣᅱ"), e)
    def bstack1lll11ll1ll_opy_(
        self,
        instance: bstack1lll1ll11ll_opy_,
        f: TestFramework,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1lll1_opy_(f, instance, bstack1llllll1lll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1llll1l_opy_.bstack1lll11ll1l1_opy_, False):
            return
        self.bstack1lllll1lll1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll11ll1l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l1111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1llllll1lll_opy_[0].name
        req.test_hook_state = bstack1llllll1lll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
        for bstack1lll1lll1ll_opy_ in bstack1lll1llllll_opy_.bstack1lll1l1llll_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11l1111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᅲ")
                if bstack1lll1lllll1_opy_
                else bstack11l1111_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᅳ")
            )
            session.ref = bstack1lll1lll1ll_opy_.ref()
            session.hub_url = bstack1lll1llllll_opy_.get_state(bstack1lll1lll1ll_opy_, bstack1lll1llllll_opy_.bstack1lll11lll1l_opy_, bstack11l1111_opy_ (u"ࠤࠥᅴ"))
            session.framework_name = bstack1lll1lll1ll_opy_.framework_name
            session.framework_version = bstack1lll1lll1ll_opy_.framework_version
            session.framework_session_id = bstack1lll1llllll_opy_.get_state(bstack1lll1lll1ll_opy_, bstack1lll1llllll_opy_.bstack1lll1l1l1ll_opy_, bstack11l1111_opy_ (u"ࠥࠦᅵ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll1llll1l_opy_.bstack1llll111111_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack11l1111_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅶ") + str(kwargs) + bstack11l1111_opy_ (u"ࠧࠨᅷ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(bstack11l1111_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅸ") + str(kwargs) + bstack11l1111_opy_ (u"ࠢࠣᅹ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll111l_opy_ = bstack1lll11l11l1_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11l1111_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅺ") + str(kwargs) + bstack11l1111_opy_ (u"ࠤࠥᅻ"))
            return
        return page
    def bstack1lll11l1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll1111ll_opy_ = {}
        for bstack1lll1lll1ll_opy_ in bstack1lll1llllll_opy_.bstack1lll1l1llll_opy_.values():
            caps = bstack1lll1llllll_opy_.get_state(bstack1lll1lll1ll_opy_, bstack1lll1llllll_opy_.bstack1lll11llll1_opy_, bstack11l1111_opy_ (u"ࠥࠦᅼ"))
        bstack1llll1111ll_opy_[bstack11l1111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤᅽ")] = caps.get(bstack11l1111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨᅾ"), bstack11l1111_opy_ (u"ࠨࠢᅿ"))
        bstack1llll1111ll_opy_[bstack11l1111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨᆀ")] = caps.get(bstack11l1111_opy_ (u"ࠣࡱࡶࠦᆁ"), bstack11l1111_opy_ (u"ࠤࠥᆂ"))
        bstack1llll1111ll_opy_[bstack11l1111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧᆃ")] = caps.get(bstack11l1111_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᆄ"), bstack11l1111_opy_ (u"ࠧࠨᆅ"))
        bstack1llll1111ll_opy_[bstack11l1111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢᆆ")] = caps.get(bstack11l1111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᆇ"), bstack11l1111_opy_ (u"ࠣࠤᆈ"))
        return bstack1llll1111ll_opy_
    def bstack1lll11lll11_opy_(self, page: object, bstack1lll11ll11l_opy_, args={}):
        try:
            bstack1lll1l11lll_opy_ = bstack11l1111_opy_ (u"ࠤࠥࠦ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠩ࠰࠱࠲ࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠭ࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡲࡪࡽࠠࡑࡴࡲࡱ࡮ࡹࡥࠩࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵ࠱ࡴࡺࡹࡨࠩࡴࡨࡷࡴࡲࡶࡦࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡿ࡫ࡴ࡟ࡣࡱࡧࡽࢂࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࢃࠩࠩࡽࡤࡶ࡬ࡥࡪࡴࡱࡱࢁ࠮ࠨࠢࠣᆉ")
            bstack1lll11ll11l_opy_ = bstack1lll11ll11l_opy_.replace(bstack11l1111_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᆊ"), bstack11l1111_opy_ (u"ࠦࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶࠦᆋ"))
            script = bstack1lll1l11lll_opy_.format(fn_body=bstack1lll11ll11l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠧࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡋࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵ࠮ࠣࠦᆌ") + str(e) + bstack11l1111_opy_ (u"ࠨࠢᆍ"))