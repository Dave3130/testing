# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l1111ll_opy_, bstack111l11ll1l1_opy_
from bstack_utils.bstack1l11ll1lll_opy_ import bstack11l111l1l1l_opy_
class bstack1l1l11l1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111ll11l_opy_=None, bstack111111l11ll_opy_=True, bstack1ll1l11ll1l_opy_=None, bstack111l111lll_opy_=None, result=None, duration=None, bstack1llll111_opy_=None, meta={}):
        self.bstack1llll111_opy_ = bstack1llll111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111l11ll_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111ll11l_opy_ = bstack111111ll11l_opy_
        self.bstack1ll1l11ll1l_opy_ = bstack1ll1l11ll1l_opy_
        self.bstack111l111lll_opy_ = bstack111l111lll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l1l1ll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11l11_opy_(self, meta):
        self.meta = meta
    def bstack11l11ll1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111lllll_opy_(self):
        bstack111111l1l1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1lllll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩἈ"): bstack111111l1l1l_opy_,
            bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩἉ"): bstack111111l1l1l_opy_,
            bstack1lllll1l_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭Ἂ"): bstack111111l1l1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1lllll1l_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡸࡱࡪࡴࡴ࠻ࠢࠥἋ") + key)
            setattr(self, key, val)
    def bstack111111l1lll_opy_(self):
        return {
            bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨἌ"): self.name,
            bstack1lllll1l_opy_ (u"ࠫࡧࡵࡤࡺࠩἍ"): {
                bstack1lllll1l_opy_ (u"ࠬࡲࡡ࡯ࡩࠪἎ"): bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭Ἇ"),
                bstack1lllll1l_opy_ (u"ࠧࡤࡱࡧࡩࠬἐ"): self.code
            },
            bstack1lllll1l_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨἑ"): self.scope,
            bstack1lllll1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧἒ"): self.tags,
            bstack1lllll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ἓ"): self.framework,
            bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨἔ"): self.started_at
        }
    def bstack111111ll1l1_opy_(self):
        return {
         bstack1lllll1l_opy_ (u"ࠬࡳࡥࡵࡣࠪἕ"): self.meta
        }
    def bstack111111l11l1_opy_(self):
        return {
            bstack1lllll1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩ἖"): {
                bstack1lllll1l_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫ἗"): self.bstack111111ll11l_opy_
            }
        }
    def bstack111111lll11_opy_(self, bstack11111l11111_opy_, details):
        step = next(filter(lambda st: st[bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࠫἘ")] == bstack11111l11111_opy_, self.meta[bstack1lllll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἙ")]), None)
        step.update(details)
    def bstack111lllll_opy_(self, bstack11111l11111_opy_):
        step = next(filter(lambda st: st[bstack1lllll1l_opy_ (u"ࠪ࡭ࡩ࠭Ἒ")] == bstack11111l11111_opy_, self.meta[bstack1lllll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἛ")]), None)
        step.update({
            bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩἜ"): bstack1l1111ll_opy_()
        })
    def bstack1lll1ll1_opy_(self, bstack11111l11111_opy_, result, duration=None):
        bstack1ll1l11ll1l_opy_ = bstack1l1111ll_opy_()
        if bstack11111l11111_opy_ is not None and self.meta.get(bstack1lllll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἝ")):
            step = next(filter(lambda st: st[bstack1lllll1l_opy_ (u"ࠧࡪࡦࠪ἞")] == bstack11111l11111_opy_, self.meta[bstack1lllll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ἟")]), None)
            step.update({
                bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧἠ"): bstack1ll1l11ll1l_opy_,
                bstack1lllll1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬἡ"): duration if duration else bstack111l11ll1l1_opy_(step[bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨἢ")], bstack1ll1l11ll1l_opy_),
                bstack1lllll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬἣ"): result.result,
                bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧἤ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111ll1ll_opy_):
        if self.meta.get(bstack1lllll1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ἥ")):
            self.meta[bstack1lllll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἦ")].append(bstack111111ll1ll_opy_)
        else:
            self.meta[bstack1lllll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἧ")] = [ bstack111111ll1ll_opy_ ]
    def bstack111111l1ll1_opy_(self):
        return {
            bstack1lllll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨἨ"): self.bstack1l1l1ll1_opy_(),
            **self.bstack111111l1lll_opy_(),
            **self.bstack111111lllll_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack111111ll111_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩἩ"): self.bstack1ll1l11ll1l_opy_,
            bstack1lllll1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭Ἢ"): self.duration,
            bstack1lllll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭Ἣ"): self.result.result
        }
        if data[bstack1lllll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧἬ")] == bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨἭ"):
            data[bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨἮ")] = self.result.bstack111111l111_opy_()
            data[bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫἯ")] = [{bstack1lllll1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧἰ"): self.result.bstack1111l1lll11_opy_()}]
        return data
    def bstack111111l1111_opy_(self):
        return {
            bstack1lllll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪἱ"): self.bstack1l1l1ll1_opy_(),
            **self.bstack111111l1lll_opy_(),
            **self.bstack111111lllll_opy_(),
            **self.bstack111111ll111_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack1l11ll11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1lllll1l_opy_ (u"࠭ࡓࡵࡣࡵࡸࡪࡪࠧἲ") in event:
            return self.bstack111111l1ll1_opy_()
        elif bstack1lllll1l_opy_ (u"ࠧࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩἳ") in event:
            return self.bstack111111l1111_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l11ll1l_opy_ = time if time else bstack1l1111ll_opy_()
        self.duration = duration if duration else bstack111l11ll1l1_opy_(self.started_at, self.bstack1ll1l11ll1l_opy_)
        if result:
            self.result = result
class bstack1lllll11_opy_(bstack1l1l11l1_opy_):
    def __init__(self, hooks=[], bstack11lll111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11lll111_opy_ = bstack11lll111_opy_
        super().__init__(*args, **kwargs, bstack111l111lll_opy_=bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹ࠭ἴ"))
    @classmethod
    def bstack111111l1l11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lllll1l_opy_ (u"ࠩ࡬ࡨࠬἵ"): id(step),
                bstack1lllll1l_opy_ (u"ࠪࡸࡪࡾࡴࠨἶ"): step.name,
                bstack1lllll1l_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬἷ"): step.keyword,
            })
        return bstack1lllll11_opy_(
            **kwargs,
            meta={
                bstack1lllll1l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪ࠭Ἰ"): {
                    bstack1lllll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫἹ"): feature.name,
                    bstack1lllll1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬἺ"): feature.filename,
                    bstack1lllll1l_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭Ἳ"): feature.description
                },
                bstack1lllll1l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫἼ"): {
                    bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨἽ"): scenario.name
                },
                bstack1lllll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἾ"): steps,
                bstack1lllll1l_opy_ (u"ࠬ࡫ࡸࡢ࡯ࡳࡰࡪࡹࠧἿ"): bstack11l111l1l1l_opy_(test)
            }
        )
    def bstack111111lll1l_opy_(self):
        return {
            bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬὀ"): self.hooks
        }
    def bstack111111l111l_opy_(self):
        if self.bstack11lll111_opy_:
            return {
                bstack1lllll1l_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ὁ"): self.bstack11lll111_opy_
            }
        return {}
    def bstack111111l1111_opy_(self):
        return {
            **super().bstack111111l1111_opy_(),
            **self.bstack111111lll1l_opy_()
        }
    def bstack111111l1ll1_opy_(self):
        return {
            **super().bstack111111l1ll1_opy_(),
            **self.bstack111111l111l_opy_()
        }
    def event_key(self):
        return bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪὂ")
class bstack1l11llll_opy_(bstack1l1l11l1_opy_):
    def __init__(self, hook_type, *args,bstack11lll111_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111ll1111_opy_ = None
        self.bstack11lll111_opy_ = bstack11lll111_opy_
        super().__init__(*args, **kwargs, bstack111l111lll_opy_=bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧὃ"))
    def bstack1l111l1l_opy_(self):
        return self.hook_type
    def bstack111111llll1_opy_(self):
        return {
            bstack1lllll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ὄ"): self.hook_type
        }
    def bstack111111l1111_opy_(self):
        return {
            **super().bstack111111l1111_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack111111l1ll1_opy_(self):
        return {
            **super().bstack111111l1ll1_opy_(),
            bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩὅ"): self.bstack1l111ll1111_opy_,
            **self.bstack111111llll1_opy_()
        }
    def event_key(self):
        return bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧ὆")
    def bstack11l1l1l1_opy_(self, bstack1l111ll1111_opy_):
        self.bstack1l111ll1111_opy_ = bstack1l111ll1111_opy_